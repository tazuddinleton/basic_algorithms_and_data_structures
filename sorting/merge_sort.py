def merge_sort(a, p, r):
    if(p < r):
        q = p+r//2
        merge_sort(a, p, q)
        merge_sort(a, q+1, r)
        # merge(a, p, q, r)


def merge(a, p, q, r):
    n1 = q-p
    n2 = r-q
    left = []
    right = []
    for i in range(0, n1):
        left.append(a[p+i])
    for j in range(0, n2):
        right.append(a[q+j])

    left.append(999999)
    right.append(999999)
    i = 0
    j = 0
    for k in range(p, r):
        print(p, r, k, i, j)
        if left[i] <= right[j]:
            a[k] = left[i]
            i = i + 1
        else:
            a[k] = right[j]
            j = j + 1


a = [6, 1, 2, 3, 4, 19, 19, 3, 32, 39, 399, 39, 21, 3, 4, 5, 2, 9]
p, q, r = 0, 0+len(a)//2, len(a)
merge(a, p, q, r)
# merge_sort(a, p, r)
