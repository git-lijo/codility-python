def solution(N, A):
    # write your code in Python 3.6
    counter = [0] * (N + 2)
    for i in A:
        if 1 <= i <= N:
            counter[i] +=1
        elif i == N+1:
            current_max = max(counter)
            counter = [current_max] * (N+2)
    counter.pop(0)
    counter.pop(N)
    return counter

print(solution(5, [3,4,4,6,1,4,4]))    