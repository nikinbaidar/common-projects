#include <stdio.h>
#include "simple_math_relations.h"

int main () {
  int num = 102 , lower = 10 , upper = 20;

  (inRange(num, lower, upper)) ? printf("Yes") : printf("No");

  return 0;
}
