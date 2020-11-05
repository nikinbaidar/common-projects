#include <stdio.h>

int mid_num(int a, int b, int c);


int main() {
    int num1;
    int num2;
    int num3;
    int result;
input:
    printf("numer 3 \"distinct\" integers ");
    scanf("%d%d%d",&num1,&num2,&num3);
    if (num1 == num2 || num2 == num3 || num3 == num1)
        goto input;
    else
        result = mid_num(num1,num2,num3);
    printf("the mid num is '%d' ",result);
    return 0;
}


int mid_num(int a, int b,int c) {
    if (a>b && a<c || a<b && a>c)
        return a;
    else if (b>a && b<c || b<a && b>c)
        return b;
    else
        return c;
}
