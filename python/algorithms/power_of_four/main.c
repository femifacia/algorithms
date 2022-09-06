#include <stdio.h>
#include <math.h>
#include <stdbool.h>


bool isPowerOfThree(int n){
    double res=log10(n)/log10(4);
    return n && (res == (int)res);
}

int main()
{
    int n = 243;
    double x=log10(n)/log10(3);
    printf("%d\n",x==(int)x);
    return (0);
}