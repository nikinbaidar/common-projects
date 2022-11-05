// This prgram does not work
#include <stdio.h>

int addPositives(int a, int b) {
  if (a > 0 && b > 0) 
    return a+b;
  return -1;
}

int main() {
  int result;
  result = addPositives(-1, 2);

  return 0;
}
