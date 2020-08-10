#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int volim()
{
    int k, n, seconds, time = 0;
	char answer, trash;
    
    if (!scanf("%d", &k) || !scanf("%d", &n))
		return 0;
    
    for (int i = 0; i < n; i++, time += seconds)
    {
        if (!scanf("%d", &seconds) || !scanf("%c", &trash) || !scanf("%c",  &answer))
			return 0;

        if (answer == 'T')
        {
            if (k == 8)
                k -= 8;
            k += 1;
        }
        
        if (time + seconds >= 210)
            return answer == 'T' ? k - 1 : k;
    }
    return 0;
}

int main(int argc, char **argv)
{
    printf("%d", volim());
    return 0;
}
