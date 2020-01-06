def areSimilar(a, b):
    diff = []
    for i in range(len(a)):
        if a[i] == b[i]:
            print('OK')
        else:
            diff.append(i)
            if len(diff) > 2:
                return False
    if len(diff) == 2:
        print(a[diff[0]] == b[diff[1]] and a[diff[1]] == b[diff[0]])
        return True if a[diff[0]] == b[diff[1]] and a[diff[1]] == b[diff[0]] else False
    if len(diff) == 0:
        return True

a = [1, 2, 3]
b = [1, 10, 2]

print(areSimilar(a, b))