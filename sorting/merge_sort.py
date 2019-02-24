

A = [1, 1, 1]
B = [2, 5, 8]


def merge(left_half, right_half, left_start, left_end, right_start, right_end):
    merged = []
    while left_start <= left_end and right_start <= right_end:
        if left_half[left_start] <= right_half[right_start]:
            merged.append(left_half[left_start])
            left_start += 1
        else:
            merged.append(right_half[right_start])
            right_start += 1

    if left_start < left_end:
        while left_start <= left_end:
            print(left_start)
            merged.append(left_half[left_start])
            left_start += 1

    if right_start < right_end:
        while right_start <= right_end:
            merged.append(right_half[right_start])
            right_start += 1
    return merged


merged = merge(A, B, 0, len(A)-1, 0, len(B)-1)
print(merged)


# def merge_sort(array, left, right):
#     count = '-'
#     if left >= right:
#         print('--->|')
#         return
#     print(count)
#     count+='-'
#     middle = (left + right)//2
#     print('merge_sort('+str(array)+str(left)+',' + str(right)+',' +str(middle)+')')
#     merge_sort(array, left, middle)
#     merge_sort(array, middle+1, right)
#     merged = merge(array,, left_start, left_end, right_start, right_end)
#     return merged

# array = [1,9,2,8,3,7,6,10,11]

# merged = merge_sort(array, 0, len(array)-1)
# print(merged)
