# Given a string S of length N shift every character by K
# positions to the right where K <= N.


def shited_string(s, k):
    l = len(s)
    sf = ['x']*l
    for i in range(l):
        sf[(i+k)%l] = s[i]

    shifted = ''
    for i in range(len(sf)):
        shifted += sf[i]
    return shifted

s = 'hacker'
k = 2

print(shited_string(s, k))