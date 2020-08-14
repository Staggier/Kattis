#include <stdio.h>
#include <stdlib.h>

void blackfriday()
{
	int n, i = 0;
	if (!scanf("%d", &n))
		return;
	
	int **dice = malloc(sizeof(int*) * 7);
	for (int i = 1; i < 7; i++)
	{
		dice[i] = malloc(sizeof(int) * 2);
		
		dice[i][0] = 0;
		dice[i][1] = 0;
	}
	
	for (i = 0; i < n; i++)
	{
		int num;
		if (!scanf("%d", &num))
			return;
			
		dice[num][0] = i + 1;
		dice[num][1] += 1;
	}
	
	int index = 0;
	for (int i = 1; i < 7; i++)
		if (dice[i][0] && dice[i][1] == 1)
			index = dice[i][0];
			
	if (!index)
		printf("none");
	else
		printf("%d", index);
}

int main(int argc, char **argv)
{
	blackfriday();
	return 0;
}
