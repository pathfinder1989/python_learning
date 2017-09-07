def calc(*num):
	sum = 0
	for n in num:
		sum = sum + n * n
	print(sum)


calc(1,2)

num = [1,2,3,4]
calc(*num)