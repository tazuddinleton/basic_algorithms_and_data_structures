## The idea is to start with an element and compare it with all other elements left side
## till the end of the array. For example if we start with 7 there are no elements to compare
## start with 3 and we have one element to the left of 3. 

def insertion_sort(a):
    for i in  range(1, len(a)):
        j = i - 1
        k = a[i]
        while j >=  0 and k < a[j]:
            a[j+1] = a[j]
            a[j] = k
            j -= 1
    return a

print(insertion_sort([7,3,1,2,4,5,6]))
