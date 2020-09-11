def solution(A):
    # write your code in Python 2.7

    N = len(A)
    ints = [0] * (N + 2)

    for num in A:
        if 1 <= num <= N:
            ints[num] += 1

    for ind in range(1, N + 2):
        if ints[ind] == 0:
            return ind

    # should never happen
    return -1
