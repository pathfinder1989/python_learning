def person(name, age, **kw):
	print('name:', name, 'age:', age, "other", kw)


person('kang', '30', city = 'from kangzhuang')


person('kang', '30', city = 'from kangzhuang', chengyuan = 'jiedilia')