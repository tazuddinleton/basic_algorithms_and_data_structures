def repeatedString(s, n):
    count = s.count('a', 0, len(s))
    rem = n % len(s)
    count = (n//len(s)) * count
    count += s[0:rem].count('a', 0, rem)
    return count


print(repeatedString('aba', 10))
