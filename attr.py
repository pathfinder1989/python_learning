#!usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
	
	def __init__(self, arg):
		self.arg = arg
		



stu = Student(12)

a = hasattr(stu, 'x')
b = hasattr(stu, 'arg')

print(a)
print(b)

