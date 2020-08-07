#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int ls(int len)
{
	double t = sqrt(len);
	if (t * t == len)
		return (int) t;
	
	int i = 1;
	while (i * i < len)
		i += 1;
	return i;
}

void grid(char* msg, int len)
{
	int count = ls(len);
	char** rows = malloc(sizeof(char*) * count);
	
	for (int i = 0; i < count; i++)
		rows[i] = malloc(sizeof(char) * (count));
	
	for (int i = count - 1, j = 0, c = 0; i >= 0; i--)
	{
		for (j = 0; j < count; j++, c++)
		{
			if (c <= len - 1)
				rows[j][i] = msg[c];
			else
				rows[j][i] = '*';
		}
	}
	
	printf("\n");
	for (int i = 0; i < count; i++)
		for (int j = 0; j < count; j++)
			if (rows[i][j] != '*')
				printf("%c", rows[i][j]);
	return;
}

void secretmessages(int cases)
{
	for (int i = 0; i < cases; i++)
	{
		char* msg = malloc(sizeof(char) * 10000);
		scanf("%s", msg);
		
		int len = strlen(msg);
		grid(msg, len);
	}
	return;
}
 
int main(int argc, char **argv)
{
	int cases;
	scanf("%d", &cases);
	
	secretmessages(cases);
	return 0;
}
