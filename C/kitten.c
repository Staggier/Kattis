#include<stdio.h>
#include<stdlib.h>
#include<string.h>

struct Node
{
    struct Node* parent;
    int val;
    struct Node** children;
};

struct Node* initNode()
{
    struct Node* node = malloc(sizeof(struct Node));
       
    node->parent = NULL;
    node->val = 0;
    node->children = NULL;
	
    return node;
}

int getInput(char** inp)
{
    char* line = calloc(200, sizeof(char));
    int c = 0;   
    while (line[0] != '-')
    {
        line = calloc(200, sizeof(char));
        inp[c++] = fgets(line, 200, stdin);
    }
    return c - 1;
}

void kitten()
{
    int branch;
    scanf("%d", &branch);
    
    char** inp = malloc(sizeof(char*) * 100);
    int n = getInput(inp);
    
    struct Node* nodes[100];
    
    for (int i = 0; i < 100; i++)
        nodes[i] = initNode();

    for (int i = 1; i < n; i++)
    {
        char* s = inp[i];
        
        int c = 0, j = 0, k = 0;
        while (s[j] != '\0')
            if (s[j++] == ' ')
                k += 1;
        
        char* str = strtok(s, " \n");
        int parent = atoi(str);
        
        while (str != NULL)
        {
            int num = atoi(str);
            if (c == 0)
            {
                nodes[parent - 1]->val = parent;
                nodes[parent - 1]->children = malloc(sizeof(struct Node*) * k);
            }
            else
            {
                nodes[num - 1]->val = num;
                nodes[num - 1]->parent = nodes[parent - 1];
                nodes[parent - 1]->children[c - 1] = nodes[num - 1];
            }
			
            str = strtok(NULL, " \n");
			c += 1;
        }
    }
    
    struct Node* node = nodes[branch - 1];
    while (node->parent)
    {
        printf("%d ", node->val);
        node = node->parent;
    }
	
    printf("%d", node->val);
    return;
}

int main()
{
    kitten();
    return 0;
}