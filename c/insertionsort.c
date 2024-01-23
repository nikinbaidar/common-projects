#include <stdio.h>
#include "array.h"

void main() {
    int x [] = {1, 7, 9, 8, 10, 33, 45};
    static unsigned int end;
    end = getEndIndex(x);
    // printf("%d", contains(1, x, end));
    printArray(x, end);
insertionSort(x, end);
    printArray(x, end);
}
