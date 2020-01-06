def sortByHeight(a):
    if len(a) == a.count(-1):
        return a
    trees = a.count(-1)
    tree_position = []
    for i in range(len(a)):
        if a[i] == -1:
            tree_position.append(i)
    a.sort()
    out = list((a[trees:]))
    for i in range(len(tree_position)):
        out.insert(tree_position[i], -1)



    return a







print(True if sortByHeight([23, 54, -1, 43, 1, -1, -1, 77, -1, -1, -1, 3]) == [1, 3, -1, 23, 43, -1, -1, 54, -1, -1, -1, 77] else False)