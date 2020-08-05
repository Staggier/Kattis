#include <stdio.h>
#include <stdlib.h>

int gcd(int a, int b) 
{ 
    if (a == 0) 
       return b; 
    if (b == 0) 
       return a; 
    if (a == b) 
        return a; 
    if (a > b) 
        return gcd(a-b, b); 
    return gcd(a, b-a); 
}

void prsteni()
{
	int n;
	scanf("%d", &n);
	
	int base;
	scanf("%d", &base);

	for (int i = 0; i < n - 1; i++)
	{
		int num;
		scanf("%d", &num);
		
		int mult = gcd(base, num);
		printf("%d/%d\n", base / mult, num / mult);
	}
	return;
}

int main(int argc, char **argv)
{
	prsteni();
	return 0;
}
