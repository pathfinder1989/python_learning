def delete_temp(s):
	return s and s.strip()

b =  filter(delete_temp, [1,'','4'])
a = list(b)
print(a)