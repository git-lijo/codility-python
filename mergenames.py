def unique_names(a, b):
	for i in b:
		if i not in a:
			a.append(i)
	return a


a = ['Ava', 'Emma', 'Olivia']
b = ['Olivia', 'Sophia', 'Emma']
print(unique_names(a,b))