#include <stdio.h>
#include "array_related_functions.h"

static int insertionSort(int x[], int n);
static int insert(int x[], int i, int a);


int insertionSort (int x[], int n) {
  if (n > 0) {
    insertionSort(x, n-1);
    insert(x, n, x[n]);
  }
  return 0;
}

int insert (int x[], int i, int a) {
  if (i == 0 || x[i-1] <= a)
    x[i] = a;
  else {
    x[i] = x[i-1];
    insert(x, i-1, a);
  }
  return 0; 
}


int main() {
  int x[] = {15, 8, 6, 3, 2, 37, 24};
  unsigned int length_x = getSize(x);

  printf("Before sorting: ");
  printArr(x, length_x);

  insertionSort(x, length_x);

  printf("\nAfter  sorting: ");
  printArr(x, length_x);
}
