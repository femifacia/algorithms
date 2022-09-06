#include <stdbool.h>
#include <stdio.h>



bool isInteger(char *s)
{
    int i = 0;
    if (!s[i])
        return(0);
    if ((s[i] == '+' || s[i] == '-') && s[i + 1])
        i++;
    for (;s[i] && s[i] <= '9' && s[i] >= '0'; i++);
    if (s[i])
        return (0);
    return (1);
}

bool isEInteger(char *s, int c)
{
    int i = 0;

    if (!s[i])
        return(0);
    for (;s[i] && s[i] <= '9' && s[i] >= '0'; i++);
    if (s[i] && (s[i] == 'e' || s[i] == 'E') && (c || i))
        return (isInteger(&(s[i+1])));
    if (s[i])
        return (0);
    return (1);
}

bool isNumber(char * s)
{
    int i = 0;
    if (!s[i])
        return(0);
    if ((s[i] == '-' || s[i] == '+') && s[i + 1])
        s++;
    for (;s[i] && s[i] <= '9' && s[i] >= '0'; i++);
    if (!s[i])
        return(1);
    if (s[i] == '.') {
        if (i == 0 && !s[1])
            return (0);
        if (i == 0 && (s[1] == 'e' || s[1] == 'E') && !s[2])
            return (0);
        if ((s[0] == '-' || s[0] == '+') && !s[i+1] && i == 1)
            return (0);
        if ((s[0] == '-' || s[0] == '+') && (s[i+1] == 'e' || s[i + 1] == 'E') && !s[i+2])
            return (0);
        if (!s[i + 1])
            return (1);
        return (isEInteger(&(s[i+ 1]), i));
    }
    if (s[i] == 'e' || s[i] == 'E') {
        if (i == 0)
            return (0);
        if ((s[0] == '-' || s[0] == '+') && i == 1)
            return (0);
        return (isInteger(&(s[i + 1])));
    }
    return (0);
}


/*
bool isInteger(char *s)
{
    int i = 0;
    if (!s[i])
        return(0);
    if ((s[i] == '+' || s[i] == '-') && s[i + 1])
        i++;
    for (;s[i] && s[i] <= '9' && s[i] >= '0'; i++);
    if (s[i])
        return (0);
    return (1);
}

bool isEInteger(char *s)
{
    int i = 0;
    if (!s[i])
        return(0);
    if ((s[i] == '+' || s[i] == '-') && s[i + 1])
        i++;
    for (;s[i] && s[i] <= '9' && s[i] >= '0'; i++);
    if (s[i] && (s[i] == 'e' || s[i] == 'E'))
        return (isInteger(&(s[i+1])));
    if (s[i])
        return (0);
    return (1);
}

bool isNumber(char * s)
{
    int i = 0;
    int c = 0;
    if (!s[i])
        return(0);
    if (s[i] == '-' || s[i] == '+')
        i++; 
    for (;s[i] && s[i] <= '9' && s[i] >= '0'; i++, c++);
    if (!s[i])
        return(1);
    if (s[i] == '.') {
        if (i == 0 && !s[1])
            return (0);
        if (i == 0 && (s[1] == 'e' || s[1] == 'E') && !s[2])
            return (0);
        if ((s[0] == '-' || s[0] == '+') && !s[i+1] && i == 1)
            return (0);
        if ((s[0] == '-' || s[0] == '+') && (s[i+1] == 'e' || s[i + 1] == 'E') && !s[i+2])
            return (0);
        if (!s[i + 1])
            return (1);
        return (isEInteger(&(s[i+ 1])));
    }
    if (s[i] == 'e' || s[i] == 'E') {
        if (i == 0)
            return (0);
        if (s[0] == '-' || s[0] == '+')
            return (0);
        return (isInteger(&(s[i + 1])));
    }
    return (0);
}
*/
int main(int argc, char **argv)
{
    if (isNumber(argv[1]))
        printf("True\n");
    else
        printf("False\n");
    return (0);
}