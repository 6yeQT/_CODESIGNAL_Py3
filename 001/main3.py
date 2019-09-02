def firstDuplicate(a):
    output = -1
    a_len = len(a)
    first_duplicate = a_len - 1
    for digit in a:
        digit_pos = a.index(digit)
        print("digit_pos ", digit_pos)
        print("first_duplicate ", first_duplicate)
        
        if digit_pos < first_duplicate:
            if a[digit_pos:first_duplicate].count(digit) > 1:
                pos_duplicate = a[digit_pos+1:first_duplicate].index(digit) + digit_pos + 1
                print("pos_duplicate ", pos_duplicate)
                if pos_duplicate < first_duplicate:
                    first_duplicate = pos_duplicate
            elif a[digit_pos] == a[first_duplicate]:
                print("out: ", first_duplicate)
                output = first_duplicate
                print(a[output])
    return a[first_duplicate] if first_duplicate != len(a)-1 else output

##a = [2, 1, 3, 5, 3, 2]
a = [2, 4, 3, 5, 1]
a = [2, 2]
a = [2, 3, 3]

print(a)
print(firstDuplicate(a))
