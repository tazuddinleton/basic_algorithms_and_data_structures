def hourglassSum(arr):
    maxSum = -99999999999999999
    for i in range(0, len(arr)-2):
        for j in range(0, len(arr[i])-2):
            sum = 0
            sum += arr[i][j]
            sum += arr[i][j+1]
            sum += arr[i][j+2]

            sum += arr[i+1][j+1]

            sum += arr[i+2][j]
            sum += arr[i+2][j+1]
            sum += arr[i+2][j+2]
            if sum > maxSum:
                maxSum = sum
    return maxSum


# input = [
#     [-9, -9, -9, 1, 1, 1],
#     [0, -9, 0, 4, 3, 2],
#     [-9, -9, -9, 1, 2, 3],
#     [0, 0, 8, 6, 6, 0],
#     [0, 0, 0, -2, 0, 0],
#     [0, 0, 1, 2, 4, 0],
# ]

input = [
    [0, -4, -6, 0, -7, -6],
    [-1, -2, -6, -8, -3, -1],
    [-8, -4, -2, -8, -8, -6],
    [-3, -1, -2, -5, 6, 0],
    [0, 0, 0, -2, 0, 0],
    [0, 0, 1, 2, 4, 0],
]
print(hourglassSum(input))
