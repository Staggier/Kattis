#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int sodaslurper(int e, int f, int c)
{
	int result = 0;
	for (int i = e + f - (c - 1); i > 0; i -= c - 1, result += 1);
	return result;
}

int main(int argc, char **argv)
{
	int e, f, c, result;
	(void)scanf("%d", &e);
	(void)scanf("%d", &f);
	(void)scanf("%d", &c);
	
	result = sodaslurper(e, f, c);
	printf("\n%d", result);
	return 0;
}
