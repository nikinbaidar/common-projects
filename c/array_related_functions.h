#define getSize(arr) sizeof(arr)/sizeof(*arr)

static int testArr [] = {0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55};

static void printArr(int *array, const size_t lengthOfArray);
static int binarySearch(int x, int *arr, int start, int end);
static int ternarySearch(int x, int *arr, int start, int end);
static int contains(int x, int *arr, const size_t lengthOfArray);


void 
printArr(int *array, const size_t lengthOfArray) 
{  
    printf("{");
    for (int i = 0; i < lengthOfArray; i++)  
        printf("%d, ", *(array+i));  
    printf("\b\b}\n");
}


int 
binarySearch(int x, int *arr, int start, int end) 
{
    /*  1. 'start' is the staring point of the search segment.
     *  2. 'end is the ending pont of the seach segment.
     *  3. When this function is first called it is start is the index of the
     *     first element, and end is the index of the last element. 
     */
    int mid;
    if (start > end) {
        /* Element 'x' was not found. */
        return -1;
    }
    else {
        mid = (int) start + (end - start) / 2;
        if (*(arr+mid) < x) 
            return binarySearch(x, arr, mid+1, end);
        else if (*(arr+mid) > x) 
            return binarySearch(x, arr, start, mid-1);
        else 
            return mid;
    }
}


int 
contains(int x, int *arr, const size_t lengthOfArray) 
{
    int result = binarySearch(x, arr, 0, lengthOfArray);
    return (result != -1);
}
