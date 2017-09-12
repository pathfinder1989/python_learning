
d = {'a':1, 'b':1, 'c':1}

for key in d:
	print(key)

#迭代value
for value in d.values():
	print(value)

#迭代key 和 value
for k, v in d.items():
	print(key , '----', v)

#针对于dict 默认情况下是迭代的key 迭代key 是无序的
