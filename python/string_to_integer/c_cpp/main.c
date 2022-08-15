#include <stdio.h>
#include <math.h>




int myAtoi(char * s){
   long res = 0;
    int mul = 1;
    int power = -1;
    int i = 0;
    int a = 0;

    while (s[i] && s[i] == ' ')
        i++;
    if (s[i] == '-') {
        mul = -1;
        i++;
    } else if (s[i] == '+')
        i++;
    while (s[i] && s[i] == '0')
        i++;
    for (a = i; s[a] && s[a] <= '9' && s[a] >= '0'; a++)
        power+=1;
    if (power >= 10 || (power == 9 && s[i] > '2')) {
        if (mul == -1)
            return (INT_MIN);
        return (INT_MAX);
    }
    if (power >= 10 && mul == -1)
        return(INT_MIN);
    s[a] = '\0';
    while (s[i] && s[i] >= '0' && s[i] <= '9') {
        res += ((s[i] - '0') * pow(10, power));
        power-=1;
        i++;
    }
    if (res * mul < INT_MIN)
        return (INT_MIN);
    if (res*mul > INT_MAX)
        return (INT_MAX);
    return (res * mul);
}

/*
int myAtoi(char * s)
{
    int res = 0;
    int mul = 1;
    int power = -1;
    int i = 0;
    int a = 0;

    while (s[i] && s[i] == ' ')
        i++;
    if (s[i] == '-') {
        mul = -1;
        i++;
    } else if (s[i] == '+')
        i++;
    while (s[i] && s[i] == '0')
        i++;
    for (a = i; s[a] && s[a] <= '9' && s[a] >= '0'; a++)
        power+=1;
    if (power >= 10) {
        return (2147483648 * mul);
    }
    s[a] = '\0';
    while (s[i] && s[i] >= '0' && s[i] <= '9') {
        res += ((s[i] - '0') * pow(10, power));
        power-=1;
        i++;
    }
    return (res * mul);
}
*/
int main(int argc, char **argv)
{
    printf("string:%s\nint: %d\n", argv[1], myAtoi(argv[1]));

    return (0);
}