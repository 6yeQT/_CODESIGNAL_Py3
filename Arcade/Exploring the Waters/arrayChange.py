def arrayChange(inputArray):
    steps = 0
    for n, i in enumerate(inputArray):
        if n != 0:
            if prev >= i:
                diff = prev - i
                steps += diff + 1
                prev += diff + 1
            else:
                prev = i
        else:
            prev = i
    return steps

# print(arrayChange([1, 1, 1]))
print(arrayChange([-1000, 0, -2, 0]))