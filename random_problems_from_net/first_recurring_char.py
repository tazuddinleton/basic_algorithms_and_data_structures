def first_recurr_char(n):
    checked = []
    for i in range(0, len(n)):
        if n[i] in checked:
            return n[i]
        checked.append(n[i])
    return None
