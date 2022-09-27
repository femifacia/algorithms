#include <stdio.h>

#define MAX 1000000 

void func(int i)
{
    if (i == MAX)
        return;
    printf("%d\n", i);
    func(i + 1);
}

int main(int argc, char **argv)
{
    func(0);
    return (0);
}