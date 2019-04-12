def insertion_sort(a):
    for i in range(1, len(a)):
        j = i - 1
        key = a[i]
        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j = j-1
        a[j+1] = key
    return a


# a = [5, 2, 6, 1, 4, 3]
b = insertion_sort([3, 9, 1, 4, 5])
print(b)
# print('before ', b)
# for i in range(0, len(b)//2):
#     k = b[i]
#     b[i] = b[len(b)-1-i]
#     b[len(b)-1-i] = k

# print('after ', b)
