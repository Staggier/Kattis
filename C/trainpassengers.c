#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* trainpassengers()
{
	int limit;
	scanf("%d", &limit);
	
	int stops;
	scanf("%d", &stops);
	
	int passengers = 0;
	for (int i = 0; i < stops; i++)
	{
		int leaving;
		scanf("%d", &leaving);
		
		int joining;
		scanf("%d", &joining);
		
		int waiting;
		scanf("%d", &waiting);
		
		if (passengers - leaving + joining <= -1)
			return "impossible";
		
		if (passengers + joining - leaving >= limit + 1)
			return "impossible";
			
		if (stops - 1 == i && (waiting != 0 || joining != 0))
			return "impossible";
			
		if (waiting != 0 && limit - (passengers + joining - leaving) != 0)
			return "impossible";
			
		passengers += joining;
		passengers -= leaving;
	}
	if (passengers != 0)
		return "impossible";
	return "possible";
}

int main(int argc, char **argv)
{
	printf("%s", trainpassengers());
	return 0;
}
