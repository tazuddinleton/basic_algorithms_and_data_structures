def jumpingOnClouds(c):
    i = 0
    jumps = 0
    while i + 1 < len(c):
        # is long jump possible
        if i + 2 < len(c) and c[i + 2] == 0:
            i += 2
            jumps += 1
        else:
            i += 1
            jumps += 1
    return jumps


print(jumpingOnClouds([0, 1, 0, 0, 0, 1, 0]))
print(jumpingOnClouds([0, 0, 1, 0, 0, 1, 0]))
