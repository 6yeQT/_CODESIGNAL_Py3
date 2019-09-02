a = [2, 1, 3, 5, 3, 2]
a = [8, 4, 6, 2, 6, 4, 7, 9, 5, 8]

def firstDuplicate(a):
    result = []
    for item in a:
        if a.count(item) > 1:
            print(item, " >1")
            pos = a.index(item)
            pos_duplicate = a[pos+1:].index(item)
            result.append(pos_duplicate+pos+1)
        else:
            result.append(-1)
    temp = -1
    for item in result:
        if item > 0 and temp == -1:
            temp = item
        elif item > 0 and item < temp:
            temp = item
        else:
            pass
        
    return a[temp] if temp>0 else -1
    
#it works
            

print(firstDuplicate(a))


##19/23 tests passed. Execution time limit exceeded on test 20: Program exceeded the execution time limit. Make sure that it completes execution in a few seconds for any possible input.
##Click the "Run Tests" button to see output, console logs, and detailed error messages for sample or custom test cases. This information is hidden when clicking the "Submit" button in order to prevent hard-coding solutions to the hidden test cases.
##Sample tests: 12/12
##Hidden tests: 7/11
##Score: 227/300
