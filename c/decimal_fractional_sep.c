/*********************************************************************************/
/* This program separates the integer part and the fractional part of a floating */
/* point integer. For example 3.14 gets separated to 3 and 0.14.                 */
/*********************************************************************************/

#include <stdio.h>
#include <stdlib.h>

void clear() {
    system("clear");
}

int main () {

    clear();

    float number;
    int integer_part;
    float fractional_part;

    number = 24.04;

    integer_part = number;
    fractional_part = number - integer_part;

    printf("Integer part is %d \n",integer_part);
    printf("Fractional part is %.2f ",fractional_part);

    return 0;

}
