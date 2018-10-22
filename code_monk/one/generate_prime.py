n = int(input())

def print_prime(n):
    collection = ''
    for i in range(1, n):
        if is_prime(i):
            collection += str(i)+' '
    print(collection)




def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
    
print_prime(n)
