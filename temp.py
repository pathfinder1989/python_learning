def power():
	print('-----')
	pass


power()



def add(a, b):
	c = a + b
	print(c)

add(1, 4)


def lifang(x, n=2):
	s = 1
	while  n > 0:
		n = n - 1
		s = s * x
		print('-----:',s)
	return s


a = lifang(3, 2)
print(a)


c = lifang(2)
print(c)