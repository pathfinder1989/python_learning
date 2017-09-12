l = list(range(1, 11))

print(l)


L = []
for x in range(1,11):
	L.append(x * x)

print(L)



a = [x*x for x in range(1,11)]
print(a)


b = [m + n for m in 'ABC' for n in 'XYZ']
print(b)