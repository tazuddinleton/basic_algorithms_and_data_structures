
# def insertion_sort(arr):
#     l = len(arr)
#     for j in range(1, l):        
#         i = j -1
#         key = arr[j]
#         while i > -1 and arr[i] > key:
#             arr[i+1] = arr[i]
#             i -= 1
#         arr[i+1] = key
#     return arr

# arr = [5,2,4,6,1,3]
# sorted_arr =  insertion_sort(arr)
# print(sorted_arr)

def insertion_sort_desc(arr):
    l = len(arr)
    for j in range(1, l):
        i = j - 1
        key = arr[j]
        while i > -1 and arr[i] < key:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key
    return arr
# desc = insertion_sort_desc(arr)
# print(desc)


def sort_desc(s, l, r):    
    arr = []
    for i in range(l, r+1):        
        arr.append(s[i])
    sorted_arr = insertion_sort_desc(arr)
    print(sorted_arr)

sort_desc('abcdef',0,5)

