def selecttion_sort(a):
    for i in range(1, len(a)-1):
        min_i = i-1
        min = a[min_i]
        for j in range(i-1, len(a)):
            if a[j] < min:
                min = a[j]
                min_i = j
                print(min)
        a[min_i] = a[i-1]
        a[i-1] = min
    return a


a = [3, 1, 5, 2, 4, 6]
b = [6, 1, 5, 2, 4, 3, 6, 7, 5, 1, 99, 999, 98, 0]
x = selecttion_sort(a)
y = selecttion_sort(b)
print(x)
print(y)
