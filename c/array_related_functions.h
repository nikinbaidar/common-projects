#define getSize(arr) sizeof(arr)/sizeof(*arr)

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





// int
// main() 
// {
//     int a [] = {5, 6, 9, 10, 13, 14, 14, 15, 16, 19, 21, 30, 31};
//     printArr(a, getSize(a));
// }
