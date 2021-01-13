#include <stdio.h>

float mid_num(float a, float b, float c);

int main() {
    float num1;
    float num2;
    float num3;
    float result;
input:
    printf("numer 3 \"distinct\" integers ");
    scanf("%f%f%f",&num1,&num2,&num3);
    if (num1 == num2 || num2 == num3 || num3 == num1)
        goto input;
    else
        result = mid_num(num1,num2,num3);
    printf("the mid num is '%0.1f' ",result);
    return 0;
}

float mid_num(float a, float b, float c) {
    if (a>b && a<c || a<b && a>c)
        return a;
    else if (b>a && b<c || b<a && b>c)
        return b;
    else
        return c;
}
