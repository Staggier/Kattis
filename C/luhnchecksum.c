#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

int luhnchecksum(char* str)
{
	int sum = 0;
	
	for (int i = strlen(str) - 1; i >= 0; i -= 2)
		sum += str[i] - '0';

	for (int i = strlen(str) - 2; i >= 0; i -= 2)
	{
		int n = (str[i] - '0') * 2;
		if (n >= 10)
			n = ((int)(n / 10)) + (n % 10);
		sum += n;
	}
	return sum;
}

int main(int argc, char **argv)
{
	int n;
	(void) scanf("%d", &n);
	
	char* result = calloc(n * 5, sizeof(char));
	for (int i = 0; i < n; i++)
	{
		char* str = malloc(sizeof(char) * 50);
		(void) scanf("%s", str);
		
		int len = strlen(str);
		str = realloc(str, sizeof(char) * (len + 1));
		str[len] = '\0';
		
		if (i == n - 1)
		{ 
			if (luhnchecksum(str) % 10 == 0)
				strcat(result, "PASS");
			else
				strcat(result, "FAIL");
		}
		else if (luhnchecksum(str) % 10 == 0)
			strcat(result, "PASS\n");
		else
			strcat(result, "FAIL\n");
	}
	
	printf("%s", result);
	return 0;
}
