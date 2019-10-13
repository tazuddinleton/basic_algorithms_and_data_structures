def partition(array, left, right, pivot):
    while(left <= right):
        while(array[left] < pivot):
            left += 1
        while(array[right] > pivot):
            right -= 1
        if(left <= right):
            elem = array[left]
            array[left] = array[right]
            array[right] = elem
            left += 1
            right -= 1
    return left


def sort(array, left, right):
    if(left >= right):
        return

    pivot = array[(left+right)//2]
    index = partition(array, left, right, pivot)
    sort(array, left, index-1)
    sort(array, index, right)


def quickSort(array):
    sort(array, 0, len(array) - 1)
    return array


print(quickSort([3, 2, 1]))
