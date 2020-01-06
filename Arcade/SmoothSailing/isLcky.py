def isLucky(n):
    strn = str(n)
    intn = [(int(letter)) for letter in strn]
    return True if sum(intn[:int(len(strn)/2)]) == sum(intn[int(len(strn)/2):]) else False



print(isLucky(1230))