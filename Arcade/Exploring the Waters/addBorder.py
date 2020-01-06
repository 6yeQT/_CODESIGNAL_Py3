def addBorder(picture):
    output = ['*'*(2 + len(picture[0]))]
    for item in picture:
        output.append('*' + item + '*')
    output.append('*'*(2 + len(picture[0])))
    return output
