def firstDuplicate(a):
    for item in a:
        a[abs(item) - 1] *= -1
        if a[abs(item) -1] > 0:
             return abs(item)
        return -1
    

a = [2, 1, 3, 5, 3, 2]
#a = [2, 4, 3, 5, 1]
#a = [2, 2]
#a = [2, 3, 3]
#a = [5, 5, 5]
#a = [1, 2, 3]

print(a)
print('output ', firstDuplicate(a))
