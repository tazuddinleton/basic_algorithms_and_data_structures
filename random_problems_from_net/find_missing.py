def find_missing(full_set, partial_set):
    xor_sum = 0
    for num in full_set:
        xor_sum ^= num
    for num in partial_set:
        xor_sum ^= num
    return xor_sum


print(find_missing([-4, 12, 9, 5, 6], [-4, 9, 12, 6]))


def reverse(str):
    str_array = []
    str_len = len(str)-1
    while(str_len > -1):
        str_array.append(str[str_len])
        str_len -= 1
    return ''.join(str_array)


print(reverse('HELLO'))
