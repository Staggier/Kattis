#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char bball()
{
	int a = 0, b = 0;
	char c;
	
	while ((c = getchar()) != EOF && (a != 10 || b != 10) && (a < 11 && b < 11))
	{
		int p = getchar() - '0';
		if (c == 'A')
			a += p;
		else if (c == 'B')
			b += p;
	}
	
	if (a != b && a > b)
		return 'A';
	else if (a != b && b > a)
		return 'B';
	
	do
	{
		int p = getchar() - '0';
		if (c == 'A')
			a += p;
		else if (c == 'B')
			b += p;
	} while ((c = getchar()) != EOF && abs(a - b) <= 1);
	
	if (a > b)
		return 'A';
	else
		return 'B';
}

int main(int argc, char **argv)
{
	printf("%c", bball());
	return 0;
}
