#include <stdio.h>

int compass()
{
	int n, k, i = 0, j = 0;
	if (!scanf("%d", &n) || !scanf("%d", &k))
		return 0;

	for (; (i + n) % 360 != k; i++);
	for (; (j + n) % 360 != k; n = n + j < 0 ? n : n + 360, j--);
	
	return i > j * -1 ? j : i;
}

int main(int argc, char **argv)
{
	printf("%d", compass());
	return 0;
}
