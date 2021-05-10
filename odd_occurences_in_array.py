def solution(A):
	paired = []
	for i in range(0,len(A)):
		if A[i] in paired:
			paired.remove(A[i])
		else:
			paired.append(A[i])

	return paired[0]

A = [9,3,9,3,9,7,9]
print(solution(A))