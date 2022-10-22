#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * Definition for a binary tree node.
 */

struct TreeNode {
     int val;
     struct TreeNode *left;
     struct TreeNode *right;
};
typedef struct t_node {
    struct TreeNode *node;
    struct t_node *next;

}t_node;

typedef struct queue {
    t_node *head;
    t_node *tail;
    int size;
}t_queue;

t_node *create_t_node(struct TreeNode *root)
{
    t_node *node = NULL;
    if (root) {
        node = (t_node *)malloc(sizeof(t_node));
        node->next = NULL;
        node->node = root;
    }
    return node;
}

void print_queue(t_queue *queue)
{
    t_node *node = queue->head;
    printf("let's print that queeeue\n");
    while (node) {
        printf("[%d] -> ", node->node->val);
        node = node->next;
    }
    printf("\n");
}

t_node *pop_t_node(t_queue *queue)
{
    t_node *tmp = queue->head;
    queue->head = (tmp) ? queue->head->next : NULL;
    if (queue->head == NULL || queue->head == queue->tail)
        queue->tail = NULL;
    queue->size -= 1;
    //printf("I pop tmp val = %d, addresse = %p", (tmp) ? tmp->node->val : -1, (tmp) ? tmp : NULL);
    //print_queue(queue);
    return tmp;
}

void add_t_node(t_queue *queue, struct TreeNode * treeNode)
{
//    printf("[%p]\n", treeNode);
/*    queue->tail->next = create_t_node(treeNode);
    queue->size += 1;
    if (queue->head == NULL)
        queue->head = queue->tail;
        */
    t_node *node = create_t_node(treeNode);
    if (!queue->head) {
        queue->head = node;
    } else {
        if (! queue->tail) 
            queue->head->next = node;
        else
            queue->tail->next = node;
        queue->tail = node;
    }
    queue->size += 1;
}

int** levelOrder(struct TreeNode* root, int* returnSize, int** returnColumnSizes){
    int level[800][500];
    int *columnSize = (int *)malloc(sizeof(int) * 800);
    t_queue to_see;
    t_node *current = NULL;
    int size_temp, i = 0;

    to_see.head = create_t_node(root);
    to_see.tail = NULL;
    to_see.size = (to_see.head) ? 1 : 0;
    while (to_see.size != 0) {
        columnSize[i] = to_see.size;
        size_temp = to_see.size;
        for (int j = 0; j < size_temp; j++) {
            current = pop_t_node(&to_see);
            //printf("%p\n", current);
            if (!current || !current->node) {
                level[i][j] = 0;
                continue;
            }
            //printf("current = %d [%p]\n", current->node->val, current->node);
            printf("%d,%d\n",i,j);
            level[i][j] = (current->node) ? current->node->val : 0;
            if (current->node->left)
                add_t_node(&to_see, current->node->left);
            if (current->node->right)
                add_t_node(&to_see, current->node->right);
            free(current);
        }
        i++;
    }
    //printf("i = %d\n", i);
    *returnSize = i;
    *returnColumnSizes = columnSize;

    while (to_see.head) {
        current = to_see.head->next;
        free(to_see.head);
        to_see.head = current;
    }
    int **level_arr = (int **)malloc(sizeof(int *) * i);
    for (int a = 0; a < i; a++) {
        level_arr[a] = (int *)malloc(sizeof(int) * columnSize[a]);
        for (int j = 0; j < columnSize[a]; j++)
            level_arr[a][j] = level[a][j];
    }
    return level_arr;
}

struct TreeNode *create_treenode(int val)
{
    struct TreeNode * node = (struct TreeNode *)malloc(sizeof(struct TreeNode));

    node->left = NULL;
    node->right = NULL;
    node->val = val;
    return (node);
}

void dfs_free(struct TreeNode *root)
{
    if (!root)
        return;
    dfs_free(root->left);
    dfs_free(root->right);
    free(root);
}

void preorder(struct TreeNode *root)
{
    if (!root)
        return;
    printf("%d\n", root->val);
    preorder(root->left);
    preorder(root->right);
}

int main(int argc, char **argv)
{
    struct TreeNode *root = create_treenode(3);
    root->left = create_treenode(9);
    root->right = create_treenode(20);
    root->right->left = create_treenode(15);
    root->right->right = create_treenode(7);
    int returnSize = 0;
    int *columnSizes = NULL;

    int **level = levelOrder(root, &returnSize, &columnSizes);
    preorder(root);
    for (int i = 0; i < returnSize; i++) {
        for (int j = 0; j < columnSizes[i]; j++)
            printf("%d ", level[i][j]);
        printf("\n");
    }
    for (int i = 0; i < 100; i++)
        free(level[i]);
    free(level);
    free(columnSizes);
    dfs_free(root);
    return 0;
}