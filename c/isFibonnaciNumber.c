/*********************************************************************************/
/* This program takes an integer number and checks if it is a fibonnaci number.  */
/* Fibonacci sequence progress as 0, 1, 1, 3, 5, 8, 13. The input is a fibonnaci */
/* number if it appears at any point in the fibonnaci sequence.                  */
/*********************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>

void clearTerminal() {
    system("clear");
}

bool isPerfectSquare (int x) {
    float root;
    int integer_part;
    float decimal_part;

    root = sqrt(x);

    integer_part = root;
    decimal_part = root - integer_part;

    return (decimal_part == 0);
}

bool isFibonnaci(int x) {
    int expression1;
    int expression2;

    expression1 = 5 * pow(x,2) + 4;
    expression2 = 5 * pow(x,2) - 4;

    return ( isPerfectSquare(expression1) || isPerfectSquare(expression2) );
}

int main() {
    clearTerminal();

    int number;

    number = 21;

    if (isFibonnaci(number))
        printf("%d is a fibonnaci number",number);
    else
        printf("%d is not a fibonnaci number",number);

    return 0;
}
