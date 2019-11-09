def rotLeft(a, d):
    for i in range(0, d):
        a.append(a.pop(0))
    return a


print(rotLeft([1, 2, 3, 4, 5], 2))
print(rotLeft([33, 47, 70, 37, 8, 53, 13,
               93, 71, 72, 51, 100, 60, 87, 97], 13))
