def strstr(s, x):
    lenS = 0
    for i in s:
        lenS += 1
    lenX = 0
    for i in x:
        lenX += 1
    if lenX > lenS:
        return -1
    temp_len_S = 0
    while temp_len_S != lenS:
        if s[temp_len_S:temp_len_S+lenX] == x:
            return temp_len_S
        temp_len_S += 1
    return -1

    