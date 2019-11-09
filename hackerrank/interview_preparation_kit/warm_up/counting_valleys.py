def countValleys(n, s):
    altitude = 0
    inAValley = False
    valleys = 0
    for i in range(0, n):
        if s[i] == 'D':
            altitude -= 1
        else:
            altitude += 1
        if altitude < 0 and not inAValley:
            valleys += 1
            inAValley = True
        if altitude >= 0:
            inAValley = False
        print(altitude)
    return valleys


##print(countValleys(8, 'UDDDUDUU'))
print(countValleys(12, 'DDUUDDUDUUUD'))
