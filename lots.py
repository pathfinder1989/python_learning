#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):
	__slots__ = ('name', 'age')
	pass

class Gra(Student):
	pass


s = Student()
s.name = 'kang'
s.age = 34

try:
	s.score = 4
except AttributeError as e:
	print('attributeError-----:', e)

g = Gra()
g.score = 90

print('g.scroe----:', g.scroe)