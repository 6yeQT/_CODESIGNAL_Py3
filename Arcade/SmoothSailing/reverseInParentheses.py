def reverseInParentheses(inputString):
    import re
    if len(inputString) <= 1:
        return inputString

    if inputString.count('(') == 0:
        return inputString

    while inputString.count('(') == inputString.count(')') and inputString.count('(') > 0:
        first = inputString.rfind('(')
        last = inputString.find(')', first)
        inputString = inputString[:first] + reverseInParentheses(inputString[first+1:last])[::-1] + inputString[last+1:]
    return inputString

# print(reverseInParentheses('123((aldjfaf)123)'))
print(reverseInParentheses('(abc)d(efg)'))



