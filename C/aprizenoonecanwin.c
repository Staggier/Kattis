#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

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

int cmpfunc (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}

int main(int argc, char **argv)
{
    char* stream = readAll();
    char* token = strtok(stream, " \n\r");
    
    int n, x, i = 0;

    n = atoi(token);
    token = strtok(NULL, " \n\r");
    x = atoi(token);
    token = strtok(NULL, " \n\r");
    
    int arr[n];
    while (i < n)
    {
        arr[i++] = atoi(token);
        token = strtok(NULL, " \n\r");
    }

    qsort(arr, n, sizeof(int), cmpfunc);
    
    int result = 1;
    for (int j = 1; j < n; j++)
    {
        if (arr[j] + arr[j - 1] > x)
            break;
        result++;
    }
    printf("%d", result);
    free(stream);
    return 0;
}
