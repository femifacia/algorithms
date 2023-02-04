#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

char **cut_str_array(char *str, char c);
char *get_file_content(char *path);
int my_array_len(char **array);


/**
 * Definition for a binary tree node.
 */

typedef struct t_node {
     int x;
     int y;
     int dist;
     struct t_node *next;
     struct t_node *prev;
}t_node;

typedef struct queue {
    t_node *head;
    t_node *tail;
    int size;
}t_queue;

t_node *create_t_node(int x, int y, int dist)
{
    t_node *node = (t_node *)malloc(sizeof(t_node));
    node->next = NULL;
    node->prev = NULL;
    node->x = x;
    node->y = y;
    node->dist = dist;
    return node;
}

void print_queue(t_queue *queue)
{
    t_node *node = queue->head;
    printf("let's print that queeeue\n");
    while (node) {
        printf("[x = %d] [y = %d] -> ", node->x, node->y);
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
    tmp->next = NULL;
    return tmp;
}

void add_t_node(t_queue *queue, t_node * node)
{
//    printf("[%p]\n", treeNode);
/*    queue->tail->next = create_t_node(treeNode);
    queue->size += 1;
    if (queue->head == NULL)
        queue->head = queue->tail;
        */
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

t_queue *create_queue(void)
{
    t_queue *queue = (t_queue *)malloc(sizeof(t_queue));

    queue->head = NULL;
    queue->tail = NULL;
    queue->size = 0;
    return queue;
}

void free_queue(t_queue *queue)
{
    t_node *current = NULL;

    while (queue->head) {
        current = queue->head->next;
        //printf("[%p] x = %d, y = %d\n", queue->head, queue->head->x, queue->head->y);
        free(queue->head);
        queue->head = current;
    }
    free(queue);
}

int nearestExit(char** maze, int mazeSize, int* mazeColSize, int* entrance, int entranceSize)
{
    int height = mazeSize;
    int width = mazeColSize[0];
    t_queue *to_see = create_queue();
    t_queue *garbage = create_queue();
    int dist = -1;
    t_node *current = NULL;
    int direction[][2] = {{1,0},{-1,0},{0,1},{0,-1}};
    int x1 = 0;
    int y1 = 0;
//    int visited[height][visited]
//    printf("%d,%d\n",width, height);
    maze[entrance[0]][entrance[1]] = '+';
    add_t_node(to_see, create_t_node(entrance[1], entrance[0], 0));
    while(to_see->size > 0) {
        current = pop_t_node(to_see);
//        print_queue(to_see);
//        printf("hehe x = %d, y = %d\n", current->x, current->y);
//        printf("then garbage");
//        print_queue(garbage);
        for (int i = 0; i < 4; i++) {
            x1 = current->x + direction[i][0];
            y1 = current->y + direction[i][1];
//            printf("%d,%d\n",x1, y1);
            if ((0 <= x1 && x1 < width) && (0 <= y1 && y1 < height) && maze[y1][x1] == '.') {
                if (x1 == entrance[1] && entrance[0] == y1)
                    continue;
                if (x1 == width -1 || x1 == 0 || y1 == 0 || y1 == height - 1) {
                    dist = current->dist + 1;
                    to_see->size = 0;
                    break;
                }
                maze[y1][x1] = '+';
                add_t_node(to_see, create_t_node(x1, y1, current->dist + 1));
            }
        }
        add_t_node(garbage, current);
    }
//    print_queue(to_see);
//    print_queue(garbage);
    free_queue(to_see);
    free_queue(garbage);
    return (dist);
}

int danteSolver(char** maze, int mazeSize, int* mazeColSize, int* entrance, int entranceSize)
{
    int height = mazeSize;
    int width = mazeColSize[0];
    t_queue *to_see = create_queue();
    t_queue *garbage = create_queue();
    int dist = -1;
    t_node *current = NULL;
    t_node *to_add = NULL;
    int direction[][2] = {{1,0},{-1,0},{0,1},{0,-1}};
    int x1 = 0;
    int y1 = 0;
    maze[0][0] = '1';
    add_t_node(to_see, create_t_node(entrance[1], entrance[0], 0));
    while(to_see->size > 0) {
        current = pop_t_node(to_see);

        for (int i = 0; i < 4; i++) {
            x1 = current->x + direction[i][0];
            y1 = current->y + direction[i][1];
            if ((0 <= x1 && x1 < width) && (0 <= y1 && y1 < height) && maze[y1][x1] == '.') {
                if (x1 == width -1 && y1 == height - 1) {
                    dist = current->dist + 1;
                    to_see->size = 0;
                    maze[height-1][width-1] = 'x';
                    break;
                }
                maze[y1][x1] = '1';
                to_add = create_t_node(x1, y1, current->dist + 1);
                to_add->prev = current;
                add_t_node(to_see, to_add);
            }
        }
        add_t_node(garbage, current);
    }
    for (int i = 0; maze[i]; i++) {
        for (int j = 0; maze[i][j]; j++) {
            if (maze[i][j] == '1')
                maze[i][j] = '.';
        }
    }
    if (dist >= 0) {
        while (current) {
            maze[current->y][current->x] = 'x';
            current = current->prev;
        }
    }
    free_queue(to_see);
    free_queue(garbage);
    return (dist);
}




int main(int argc, char **argv)
{
    char *file = get_file_content(argv[1]);
    char **maze = cut_str_array(file, '\n');
    int mazeSize = my_array_len(maze);
    int mazeColSize = strlen(maze[0]);
    int entreance[2] = {0, 1};
//    char maze[][10] = {".........", ".........", "........."};
    printf("before\n");
    for (int i = 0; maze[i]; i++)
        printf("%s\n", maze[i]);
    printf("after\n");
    printf("%d\n", danteSolver(maze, mazeSize,&mazeColSize,entreance,2));
    for (int i = 0; maze[i]; i++)
        printf("%s\n", maze[i]);
//    if (0 < -1  && maze[50][50])
//        printf("ok");
    free(file);

    for (int i = 0; maze[i]; i++)
        free(maze[i]);
    free(maze);
    return 0;
}