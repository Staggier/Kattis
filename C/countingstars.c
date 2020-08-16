#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int height, width, result;
// Return 1 iff (x,y) are valid coordinates in the game.
int inbounds(int x, int y) 
{
    return x >= 0 && x < height && y >= 0 && y < width;
}

void floodfill(char** lines, int x, int y)
{
     int i;
     lines[x][y] = '#';

     for (i = -1; i < 2; i++)
     {
         if (inbounds(x + i, y) && lines[x + i][y] == '-')
             floodfill(lines, x + i, y);
     }
     for (i = -1; i < 2; i++)
     {
         if (inbounds(x, y + i) && lines[x][y + i] == '-')
             floodfill(lines, x, y + i);
     }
}

char* readAll()
{
    unsigned long long int maxSize     = 2,
                           currentSize = 0;

    char* str = calloc(maxSize, sizeof(char));
    char c = '\0';
    while ((c = getchar()) != EOF)
    {
        str[currentSize++] = c;
        if (currentSize == maxSize - 1)
        {
            maxSize *= 2;
            str = realloc(str, maxSize * sizeof(char));
        }
    }
    
    str = realloc(str, (currentSize + 1) * sizeof(char));
    str[currentSize] = '\0';
    
    return str;
}

int main(int argc, char **argv)
{
    char* stream = readAll();
    char* token = strtok(stream, " \n");
    
    int numcases = 1;
    while (token != NULL)
    {
        char** grid;
        
        height = atoi(token);
        token = strtok(NULL, " \n\r");
        width = atoi(token);
        token = strtok(NULL, " \n\r");
        
        grid = malloc(sizeof(char*) * height);
        result = 0;
        
        for (int i = 0, j = 0; i < height; i++)
        {
            grid[i] = malloc(sizeof(char) * (width + 1));
            for (j = 0; j < width; j++)
                grid[i][j] = token[j];
                
            grid[i][j] = '\0';
            token = strtok(NULL, " \n");
        }
        
        for (int i = 0; i < height; i++)
            for (int j = 0; j < width; j++)
                if (grid[i][j] == '-')
                {
                    floodfill(grid, i, j);
                    result++;
                }
        
        printf("Case %d: %d\n", numcases++, result);
        
        for (int i = 0; i < height; i++)
            free(grid[i]);
        free(grid);
    }
    return 0;
}