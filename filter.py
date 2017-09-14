def temp(n):
	return n == 3


a = filter(temp, [1,2,3,4,56])
b = list(a)
print(b)