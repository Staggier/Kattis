#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int sifferprodukt(int n)
{
	if (n < 10)
		return n;
		
	int result = 1;
	char* s = malloc(sizeof(char) * 5);
	
	sprintf(s, "%d", n);
	
	for (int i = 0; i < strlen(s); i++)
		result *= s[i] == '0' ? 1 : s[i] - '0';
	return sifferprodukt(result);
}

int main(int argc, char **argv)
{
	int n;
	scanf("%d", &n);
	
	printf("%d", sifferprodukt(n));
	return 0;
}
