#define getEndIndex(arr) (sizeof(arr)/sizeof(*arr) - 1)


const short int start = 0;

/* Function Definitions */

static void insert(int arr[], int i, int a);
static void insertionSort(int arr[], int end);
static void printArray(int *array, const size_t lengthOfArray);
static int binarySearch(int x, int *arr, int start, int end);
static int ternarySearch(int x, int *arr, int start, int end);
static int contains(int x, int *arr, const size_t lengthOfArray);


void insert (int arr[], int i, int a) {
    if (arr[i-1] <= a || i == 0)
        arr[i] = a;
    else {
        arr[i] = arr[i-1];
        insert(arr, i-1, a);
    }
}


void insertionSort(int arr[], int end) {
    /* Insertion sort is only scaleable for shorter arrays! */
    if (end > 1) {
        insertionSort(arr, end-1);
        insert(arr, end, arr[end]);
    }
}


void printArray(int *array, const size_t lengthOfArray) {  
    printf("\n{");
    for (int i = 0; i <= lengthOfArray; i++)  { printf("%d, ", *(array+i)); }
    printf("\b\b}");
}


int binarySearch(int x, int *arr, int start, int end) {
    /*  1. 'start' is the staring point of the search segment.
     *  2. 'end is the ending point of the search segment.
     *  3. When this function is first called, start is the index of the
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


int contains(int x, int *arr, const size_t arrayEndIndex) {
        int result = binarySearch(x, arr, start, arrayEndIndex);
        return (result != -1);
}
