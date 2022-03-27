/*********************************************************************************/
/* This program separates the integer part and the fractional part of a floating */
/* point integer. For example 3.14 gets separated to 3 and 0.14.                 */
/*********************************************************************************/

#include <stdio.h>
#include <stdlib.h>

int main () {

    float number;
    int integer_part;
    float fractional_part;

    number = 3.14;

    integer_part = number;
    fractional_part = number - integer_part;

    printf("Integer part    = %d  \n", integer_part);
    printf("Fractional part = %.2f\n", fractional_part);

    return 0;

}
