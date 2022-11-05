#define getSize(arr) sizeof(arr)/sizeof(*arr)

void printPtrArr(int *array, int length) 
{  
    printf("{");
    for (int i = 0; i < length; i++)  
        printf("%d, ", *(array+i));  
    printf("\b\b}\n");
}


void printArr(int array[], int length) 
{  
    printf("{");
    for (int i = 0; i < length; i++)  
        printf("%d, ", array[i]);  
    printf("\b\b}\n");
}
