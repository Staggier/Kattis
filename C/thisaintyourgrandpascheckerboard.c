#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char** getBoard(int size)
{
	char** board = malloc(sizeof(char*) * size);
	for (int i = 0, j = 0; i < size; i++)
	{
		char* row = malloc(sizeof(char) * (size + 2));
		for (j = 0; j < size; j++)
			row[j] = getchar();
		row[j] = getchar();

		row[j + 1] = '\0';
		board[i] = row;
	}
	return board;
}

int validRow(char** grid, int size)
{
	char last;
	for(int i = 0; i < size; i++)
	{
		int b = 0, c = 0, w = 0;
		for (int j = 0; j < size; j++)
		{
			char ch = grid[i][j];
			if (ch == 'W') 
				w += 1;
			else 
				b += 1;
			
				
			if (ch == last)
			{
				c += 1;
				if (c >= 3) 
					return 0;
			}
			else c = 1;
			last = ch;
		}
		if (b != w) return 0;
	}
	return 1;
}

int validCol(char** grid, int size)
{
	char last;
	for(int i = 0; i < size; i++)
	{
		int b = 0, c = 0, w = 0;
		for (int j = 0; j < size; j++)
		{
			char ch = grid[j][i];
			if (ch == 'W') 
				w += 1;
			else 
				b += 1;
			
			if (ch == last)
			{
				c += 1;
				if (c >= 3) 
					return 0;
			}
			else c = 1;
			last = ch;
		}
		if (b != w) return 0;
	}
	return 1;
}

int validGrid(char** grid, int size)
{
	return validRow(grid, size) * validCol(grid, size);
}

int main(int argc, char **argv)
{
	int size;
	scanf("%d", &size);
	getchar();
	
	char** grid;
	grid = getBoard(size);
	
	printf("%d", validGrid(grid, size));
	return 0;
}
