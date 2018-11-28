def stringify(arr):
    s = ''
    for i in range(len(arr)):
        s+= arr[i]
    return s

def sort_desc(s):    
    l = len(s)
    arr = []
    for i in range(l):
        arr.append(s[i])
    for j in range(1, l):
        k = j - 1
        key = arr[j]
        while k > - 1 and arr[k] < key:
            arr[k+1] = arr[k]
            k = k - 1
        arr[k+1] = key        
    return stringify(arr)

def get_sorted_sub(s, l, r):
    f = s[0:l]
    m = sort_desc(s[l:r])
    e = s[r:len(s)]            
    return f+m+e

t = int(input())
ans = ''
while t > 0:
    s = input()
    s = s.split(' ')    
    l = int(s[1]) 
    r = int(s[2]) 
    s = s[0]
    s = get_sorted_sub(s, l, r+1)
    ans += s
    ans += '\n'
    t -= 1
print(ans)
