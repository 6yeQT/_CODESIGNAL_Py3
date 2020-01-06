def classifyStrings(s):
    import re
    if re.findall('(([aeiou]{3})|[^aeiou\?]{5})', s):
        return 'bad'
    if '?' in s:
        a = classifyStrings(s.replace('?', 'a', 1))
        b = classifyStrings(s.replace('?', 'n', 1))
        return a if a == b else 'mixed'
    return 'good'

print('FINAL: ', classifyStrings('a??u'))
print('FINAL: ', classifyStrings('aa?bbb?a?bbb?a?bbb?a'))

