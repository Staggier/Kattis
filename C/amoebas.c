#include <stdio.h> 
#include <stdlib.h> 
#include <string.h> 
#include <ctype.h> 

int height, width;

int inbounds(int x, int y) 
{ 
    return x >= 0 && x < height && y >= 0 && y < width; 
} 

void floodfill(char** grid, int x, int y) 
{ 
    int i, j; 
    grid[x][y] = '.'; 

    for (i = -1; i < 2; i++) 
        for (j = -1; j < 2; j++)
            if (inbounds(x + i, y + j) && grid[x + i][y + j] == '#') 
                floodfill(grid, x + i, y + j); 
}

char** grid(int x, int y)
{ 
    char **lines = malloc(sizeof(char*) * y);
    for (int i = 0; i < y; i++)
    {
        char* line = malloc(sizeof(char) * (x + 1));
        scanf("%s", line);
        lines[i] = line;
    }
    return lines;
}

int amoebas()
{
    int x, y;
    
    scanf("%d", &y);
    scanf("%d", &x);
    
    height = y;
    width = x;
    
    char **lines = grid(x, y);
    int result = 0;
    
    for (int i = 0; i < y; i++)
        for (int j = 0; j < x; j++)
            if (lines[i][j] == '#')
            {
                floodfill(lines, i, j);
                result += 1;
            }
    return result;
}

int main()
{
    printf("%d", amoebas());
    return 0;
}