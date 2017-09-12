it = iter([1,12,3,4])
while True:
	try:
		x = next(it)
	except StopIteration:
		break