#include <stdio.h>
#include <stdlib.h>

int cmpfunc (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}

int akcija()
{
	int lines;
	scanf("%d", &lines);
	
	int* ptr = malloc(sizeof(int) * lines);
	for (int i = 0; i < lines; i++)
	{
		int num;
		int temp = scanf("%d", &num);
		
		ptr[i] = num;
	}
	
	qsort(ptr, lines, sizeof(int), cmpfunc);
	
	int result = 0;
	for (int i = lines - 1, j = 0; i >= 0; i--)
	{
		if (j != 2)
			result += ptr[i];
		j = j == 2 ? 0 : j + 1;
	}
	
	return result;
}

int main(int argc, char **argv)
{
	printf("%d", akcija());
	return 0;
}
