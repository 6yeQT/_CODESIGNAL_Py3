def firstDuplicate(a):
    output = -1
    for item in a:
        if a.count(item) > 1:
            pos = a.index(item)
            pos_duplicate = a[pos+1:].index(item) + pos + 1
            if output == -1 and pos_duplicate > -1:
                output = pos_duplicate
            elif pos_duplicate < output:
                output = pos_duplicate
    return a[output] if output !=-1 else -1


##20/23 tests passed. Execution time limit exceeded on test 21: Program exceeded the execution time limit. Make sure that it completes execution in a few seconds for any possible input.
##Click the "Run Tests" button to see output, console logs, and detailed error messages for sample or custom test cases. This information is hidden when clicking the "Submit" button in order to prevent hard-coding solutions to the hidden test cases.
##Sample tests: 12/12
##Hidden tests: 8/11
##Score: 245/300
##2,000
