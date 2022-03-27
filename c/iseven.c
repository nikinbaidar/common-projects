/*       _\|/_
         (o o)
 +----oOO-{_}-OOo----------------+
 |Just a trivial program this is.|
 +------------------------------*/

#include <stdio.h>

#define isEven(integer) !(integer&1)

int main() {
  int number;

  printf("Enter a number: ");
  scanf("%d", &number);

  if (isEven(number))
    printf("%d is Even", number);
  else
    printf("%d is Odd", number);

  return 0;
}
