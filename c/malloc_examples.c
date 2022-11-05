/* malloc() stores 8 bytes of metadata, holding information about the number of
 * blocks allocated, before the space that actually gets allocated. The minimum
 * amout of memory reserved is 32 bytes (for x86_64 systems) and is always a
 * multiple of 16 after that. This means at least 6 integers (each of 4 byte)
 * can be stored in an array created using malloc; because (i) 4 * 6 = 24, and
 * (ii) 24 + 8 = 32.
 */

#include <stdio.h>
#include <stdlib.h>

#include "array_related_functions.h"
#include "simple_math_relations.h"

/* Function Declarations */

static void mymalloc(int bytesToAllocate);
static void getRange(int sizeAllocated);

/* Function Defs */

void mymalloc(int bytesToAllocate) {
  static short int sizeMetadata = 8; // bytes

  bytesToAllocate += sizeMetadata;

  if (! isFactor(bytesToAllocate, 16)) 
    bytesToAllocate = (bytesToAllocate / 16 + 1) * 16;
    if (bytesToAllocate < 32) // 32 is minimum for x86_64
      bytesToAllocate = 32;

  printf("Memory alocated = %d bytes\n", bytesToAllocate);
}


void getRange(int sizeAllocated) {

}


int main() {

  int *a;
  int *metadata_location;
  static int n;
  static int sizeAllocated;

  n = 11;
  a = (int*) malloc(n * sizeof(int));
  metadata_location = a - 2;

  for (int i = 0; i < n ; i++)
    a[i] = i + 1;
  printPtrArr(a, n);

  printf("%d \n", *(metadata_location) - 1) ; // indexing starts from 0

  free(a);

  mymalloc(n * sizeof(int));

  return 0;

}
