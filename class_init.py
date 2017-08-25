#!/usr/bin/python
# _*_coding: utf-8 _*_
#__init__是个初始化方法

class Person():
	def __init__(self, name):
		self.name = name
		print '初始化就执行这个'
	def sayHi(self):
		print 'hello my name is ', self.name



p = Person('kangbo')
p.sayHi();
		