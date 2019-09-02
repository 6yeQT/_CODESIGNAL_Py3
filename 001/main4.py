def firstDuplicate(a):
    output = -1
    a_len = len(a)
    mark = a_len
    
    for digit in a:
        view_range = len(a[a.index(digit):mark])
        print('view_range ', view_range)
        print('mark ', mark)
        print('digit ', digit)
        if view_range > 1:
            for i in range(a.index(digit)+1, mark):
                if digit == a[i]:
                    print('granted')
                    output = digit
                    mark = i
        elif len(a) == 2:
            output = a[0] if a[0] == a[1] else -1
        print('output ', output)
    return output
    
    

a = [2, 1, 3, 5, 3, 2]
##a = [2, 4, 3, 5, 1]
##a = [2, 2]

print(a)
print(firstDuplicate(a))
