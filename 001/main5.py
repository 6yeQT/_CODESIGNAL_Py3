def firstDuplicate(a):
    checked = False
    out = -1
    a_len = len(a)

    for i in range(0, a_len):
        for j in range(i+1, a_len):
            if a[i] == a[j]:
                checked = True
                if out == -1:
                    out = j
                elif j < out:
                    out = j
                break
            
    return a[out] if checked == True else -1

    

a = [2, 1, 3, 5, 3, 2]
#a = [2, 4, 3, 5, 1]
#a = [2, 2]
#a = [2, 3, 3]
#a = [5, 5, 5]
#a = [1, 2, 3]

print(a)
print('output ', firstDuplicate(a))
