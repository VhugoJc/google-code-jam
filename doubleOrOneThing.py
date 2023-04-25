T = int(input())  # read the number of test cases

# loop over each test case
for case in range(T):
    S = input()  # read the string for the current test case
    result = []  # initialize a list to store the resulting string
    count = 1  # initialize a counter for consecutive characters

    # loop over each character in the string
    for i in range(len(S)):
        # check if the current character is not the last one in the string
        if i + 1 != len(S):
            # check if the current and next characters are the same
            if S[i] == S[i+1]:
                count += 1  # increment the counter
            else:
                # if the current character is lexicographically smaller than the next one,
                # add count copies of the current character to the result
                if S[i] < S[i+1]:
                    result.append(S[i] * count)
                count = 1  # reset the counter

        # add the current character to the result
        result.append(S[i])

    # print the resulting string for the current test case
    print('Case #%d: %s' % (case+1, "".join(result)))
