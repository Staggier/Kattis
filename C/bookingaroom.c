#include <stdio.h>
#include <stdlib.h>

void bookingaroom()
{
	int limit;
	scanf("%d", &limit);
	
	int items;
	scanf("%d", &items);
	
	if (limit == items)
	{
		printf("too late");
		return;
	}
	
	int* ptr = calloc(limit, sizeof(int));
	for (int i = 0; i < items; i++)
	{
		int num;
		scanf("%d", &num);
		
		ptr[num] = 1;
	}
	
	for (int i = 0; i < limit; i++)
		if (!ptr[i + 1])
		{
			printf("%d", i + 1);
			return;
		}
	return;
}

int main(int argc, char **argv)
{
	bookingaroom();
	return 0;
}
