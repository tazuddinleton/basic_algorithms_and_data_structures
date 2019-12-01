
def minimumBribes(a):
    isSorted = False
    count = 0
    end = len(a)-1
    while not isSorted:
        isSorted = True        
        for i in range(0, end):
            if a[i] - (i+1) > 2:
                print('Too chaotic')
                return
            if a[i] > a[i+1]:
                isSorted = False
                count += 1
                t = a[i]
                a[i] = a[i+1]
                a[i+1] = t
        end -= 1
    print(count)





# def minimumBribes(q):    
#     br = 0
#     for i in range(0, len(q)):                
#         if q[i] - (i+1) > 2:
#             print('Too chaotic')
#             return        
#     ## Look back and count for each person how many people have over taken him
#         for j in range(0, i):
#             if q[j] > q[i]:
#                 br += 1
#     print(br)
    
minimumBribes([2,1,5,3,4])

minimumBribes([2,5,1,3,4])
minimumBribes([1,2,3,5,4,6,7,8])
minimumBribes([1,2,5,3,4,6,7,8])
minimumBribes([1,2,5,3,4,7,6,8])
minimumBribes([1,2,5,3,7,8,6,4])

