def solution(A, K):
	while K!=0:
		n = len(A)
		if n == 0:
			return A
		last = A[len(A)-1]
		for i in range(n-2,-1,-1):
			A[i+1] = A[i]
		A[0] = last
		K=K-1

	return A

A = [3, 8, 9, 7, 6]
K=1
print(solution([],1))