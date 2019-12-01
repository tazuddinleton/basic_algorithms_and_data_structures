#include <stdio.h>
void display_array(int arr[], int array_size);
void bubble_sort(int a[], int len);
void main()
{
    int array_size = 5;
    int a[] = {5, 4, 3, 2, 1};
    bubble_sort(a, array_size);    
    display_array(a, array_size);
}

void display_array(int arr[], int array_size){
    for (int i = 0; i < array_size; i++)
    {
        printf("%d\n", arr[i]);
    }
}
void bubble_sort(int a[], int len){
    short isSorted = 0;
    while(!isSorted){
        isSorted = 1;
        for(int i = 0; i < len; i++){
            if(a[i] > a[i+1]){
                isSorted = 0;
                int t = a[i];
                a[i] = a[i+1];
                a[i+1] = t;                
            }
        }
    }
}