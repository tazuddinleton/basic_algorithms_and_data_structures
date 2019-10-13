def sockMerchant(n, ar):

    socks = dict()
    count_pairs = 0
    for i in range(0, n):
        sock = ar[i]
        if sock in socks:
            socks[sock] += 1
        else:
            socks[sock] = 1
    for key in socks:
        pairs = socks[key]
        while pairs >= 2:
            pairs -= 2
            count_pairs += 1
    return count_pairs


print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
