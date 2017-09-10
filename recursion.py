def fact(n):
	if n == 1:
		return 1
	return n * fact(n - 1)


a = fact(1)
print(a)

a = fact(5)
print(a)