#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

double groupScore(int* scores, int n);
double averageScore(int* scores, int n);

double averageScore(int* scores, int n)
{
	double result = 0;
	for (int i = 0; i < n; i++)
	{
		int* group = malloc(sizeof(int) * (n - 1));
		for (int j = 0, k = 0; j < n; j++)
		{
			if (j == i)
				continue;
			group[k++] = scores[j];
		}

		result += groupScore(group, n - 1);
	}
	
	return result / n;
}

double groupScore(int* scores, int n)
{
	double result = 0;
	for (int i = 0; i < n; i++)
		result += scores[i] * (pow(4, i) / pow(5, i));
	
	result *= (1.0/5.0);
	return result;
}

int* getScores(int n)
{
	int* scores = malloc(sizeof(int) * n);
	for (int i = 0; i < n; i++)
	{
		int num;
		scanf("%d", &num);
		scores[i] = num;
	}
	
	return scores;
}

int main(int argc, char **argv)
{
	int n;
	scanf("%d", &n);
	
	int* scores = getScores(n);
	double classScore = groupScore(scores, n);
	double avgScore = averageScore(scores, n);
	
	printf("\n%f\n%f", classScore, avgScore);
	return 0;
}
sor