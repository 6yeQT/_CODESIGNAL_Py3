def isCryptSolution(crypt, solution):

    def letters2digits(input, output):
        temp = ''
        for i in input:
            for item in output:
                if i == item[0]:
                    temp += item[1]
        return temp

    decrypt = []
    for item in crypt:
        decrypt.append(letters2digits(item, solution))

    if (decrypt[0][0] == '0' and len(decrypt[0]) > 1) or (decrypt[1][0] == '0' and len(decrypt[1]) > 1)\
            or (decrypt[2][0] == '0' and len(decrypt[2]) > 1):
        return False

    if int(decrypt[0]) + int(decrypt[1]) == int(decrypt[2]):
        return True
    else:
        return False



crypt = ["TEN",
        "TWO",
        "ONE"]
solution = [["O","1"],
         ["T","0"],
         ["W","9"],
         ["E","5"],
         ["N","4"]]

print('PASS') if isCryptSolution(crypt, solution) else print('FAIL')
