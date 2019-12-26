def amendTheSentence(s):
    out = ''
    for letter in s:
        if letter.isupper():
            out += ' ' + letter.lower()
        else:
            out += letter
    return out.strip()
