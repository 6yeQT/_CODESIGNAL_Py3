def commonCharacterCount(s1, s2):
    count = 0
    done = []

    for i in range(len(s1)):
        if s1[i] not in done:
            count += min([s1.count(s1[i]), s2.count(s1[i])])

            print(s1[i], ' ', s2[i], ' ', count)
            done.append(s1[i])
    return count

print(commonCharacterCount('aabcc', 'adcaa'))