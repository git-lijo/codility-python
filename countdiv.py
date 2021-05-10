

def solution(A, B, K):
    # write your code in Python 3.6
    b = B//K
    a = (A - 1)//K if (A > 0) else 0
    if A == 0:
    	b+=1

    return b - a


A=6
B=11
print(solution(A, B, 11))

# Explanation: Number of integer in the range [1 .. X] that divisible by K is X/K. So, within the range [A .. B], the result is B/K - (A - 1)/K

# In case A is 0, as 0 is divisible by any positive number, we need to count it in.