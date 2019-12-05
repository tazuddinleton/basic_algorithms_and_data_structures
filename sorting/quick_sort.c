
/*
    Quick Sort

    1. Pick a pivot 
    2. Send elements that are less than pivot to the left
    3. Send elements that are greater than pivot to the right
    4. Now repeat the process with each sub array (before pivot and after pivot)

*/

#include <stdio.h>

int partition(int array[], int start, int end, int pivot);
void quickSort(int array[], int start, int end);
void printArray(int array[], int len);

int main(char *args[])
{
    
    int array[] = {5, 4, 1, 2, 9, 2, 8};
    quickSort(array, 0, 6);
    printArray(array, 6);
    return 0;
}

int partition(int array[], int start, int end, int pivot)
{
    while (start <= end)
    {        
        while (array[start] < pivot)
        {     
            start++;
        }

        while (array[end] > pivot)
        {            
            end--;
        }

        if (start <= end)
        {
            int elem = array[start];
            array[start] = array[end];
            array[end] = elem;

            start++;
            end--;
        }
    }
    return start;
}

void quickSort(int array[], int start, int end)
{
    if (start < end)
    {
        int pivot = array[(start + end) / 2];
        int pIndex = partition(array, start, end, pivot);
        quickSort(array, start, pIndex - 1);
        quickSort(array, pIndex, end);
    }
}


