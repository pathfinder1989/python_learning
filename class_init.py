#!/usr/bin/python
# _*_coding: utf-8 _*_
#__init__是个初始化方法

class Person():
	"""docstring for name"""
	def __init__(self, name):
		self.name = name
		def sayHi(self):
			print 'hello my name is ', self.name



p = Person('kangbo')
p.sayHi();
		