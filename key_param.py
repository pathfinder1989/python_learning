def person(name, age, **kw):
	print('name:', name, 'age:', age, "other", kw)


#person('kang', '30', city = 'from kangzhuang')


#person('kang', '30', city = 'from kangzhuang', chengyuan = 'jiedilia')



def person(name, age, **kw):
	if 'city' in kw:
		print('has city param')


	print('name %s age %s other %s') % name, age , kw


person('jack', 24 , city='beijing')