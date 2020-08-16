#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
int len = 0;

int getIndex(char val)
{
	for (int i = 0; i < 26; i++)
		if (alpha[i] == val)
			return i;
	return -1;
}

char** divide(char* str)
{
	char** strings = malloc(sizeof(char*) * 2);
	len = strlen(str) / 2;
	
	for (int i = 0, j = 0, c = 0; i < 2; i++)
	{
		char* s = malloc(sizeof(char) * (len + 1));
		for (c = 0; c < len; c++, j++)
			s[c] = str[j];
		s[c] = '\0';
		strings[i] = s;
	}
	return strings;
}

char** rotate(char** strings)
{
	char** result = malloc(sizeof(char*) * 2);
	for (int i = 0, c = 0; i < 2; i++)
	{
		char* s = malloc(sizeof(char) * (len + 1));
		int sum = 0;
		
		for (c = 0; c < len; c++) 
			sum += getIndex(strings[i][c]);
		
		for (c = 0; c < len; c++)
			s[c] = alpha[(sum + getIndex(strings[i][c])) % 26];
		s[c] = '\0';
		result[i] = s;
	}
	return result;
}

char* merge(char** strings)
{
	char* result = malloc(sizeof(char) * (len + 1));
	int c = 0;
	
	for (c = 0; c < len; c++)
		result[c] = alpha[(getIndex(strings[0][c]) + getIndex(strings[1][c])) % 26];

	result[c] = '\0';
	return result;
}

int main(int argc, char **argv)
{
	char* s = malloc(sizeof(char) * 15000);
	scanf("%s", s);
	
	char** strings = divide(s);
	strings = rotate(strings);

	char* ans = merge(strings);
	printf("%s", ans);
	return 0;
}
