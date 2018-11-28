def reverse(str):
    reverse = ""
    l = len(str)
    while(l > 0):
        l -= 1
        reverse += str[l]
    return reverse


def is_palindrom(str):
    if(str == reverse(str)):
        return True
    return False

string = 'RACECAR'
string1 = 'KUALALAMPUR'
string2 = '1991'
print(is_palindrom(string))
print(is_palindrom(string1))
print(is_palindrom(string2))

