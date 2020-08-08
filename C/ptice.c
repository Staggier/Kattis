#include <stdio.h>
#include <stdlib.h>

void ptice()
{
	char adrian[3] = {'A', 'B', 'C' }, bruno[4] = {'B', 'A', 'B', 'C' }, goran[6] = {'C', 'C', 'A', 'A', 'B', 'B'};
	int size;
	
	scanf("%d", &size);
	char* s = malloc(sizeof(char) * size);
	
	scanf("%s", s);
	
	int a = 0, b = 0, g = 0;
	for (int i = 0; i < size; i++)
	{
		if (s[i] == adrian[i % 3])
			a += 1;
		if (s[i] == bruno[i % 4])
			b += 1;
		if (s[i] == goran[i % 6])
			g += 1;
	}
	
	int arr[3] = {a, b, g};
	char* str[3] = {"Adrian", "Bruno", "Goran"};
	
	int m = a > b ? a > g ? a : g : b > g ? b : g;
	printf("%d\n", m);
	
	for (int i = 0; i < 3; i++)
		if (arr[i] == m)
			printf("%s\n", str[i]);
	return;
}

int main(int argc, char **argv)
{
	ptice();
	return 0;
}
