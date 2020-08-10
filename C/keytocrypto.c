#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char decrypt(char c, char key)
{
  c += (key > c) ? 26 : 0;
  return (((c - 'A') - (key - 'A')) % 26) + 'A';
}

char* keytocrypto()
{
	char *ciphertext = malloc(sizeof(char) * 501), *key = malloc(sizeof(char) * 1001);
	if (!scanf("%s", ciphertext))
		return NULL;
	
	int len = strlen(ciphertext) + 1;
	ciphertext = realloc(ciphertext, sizeof(char) * (len));

	if (!scanf("%s", key))
		return NULL;
	
	char* msg = malloc(sizeof(char) * len);
	
	int i = 0, j = strlen(key);
	while (ciphertext[i])
	{
		int index = decrypt(ciphertext[i], key[i]);

		msg[i++] = index;
		key[j++] = index;
	}
	
	key[i] = '\0';
	msg[i] = '\0';
	return msg;
}

int main(int argc, char **argv)
{
	printf("%s", keytocrypto());
	return 0;
}
