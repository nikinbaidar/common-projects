#include <stdio.h>
#include "array.h"

void main() {
    int myArray [] = {2, 6, 4, 0, 5, 1, 3};
    const int end = getEndIndex(myArray);
    insertionSort(myArray, end);
    printArray(myArray, end);
}
