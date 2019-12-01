
def bubbleSort(a):
    isSorted = False    
    while not isSorted:
        isSorted = True
        for i in range(0, len(a)-1):
            if a[i] > a[i+1]:
                isSorted = False                
                t = a[i]
                a[i] = a[i+1]
                a[i+1] = t
    return a


# bubbleSort([2,5,1,3,4])
# bubbleSort([2,1,5,3,4])
# bubbleSort([1,2,3,5,4,6,7,8])
# bubbleSort([1,2,5,3,7,8,6,4])
