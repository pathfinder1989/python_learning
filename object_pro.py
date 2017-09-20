#!/usr/bin/env python3
# -*- coding: utf-8 _*_


class Student(object):
	pass

#给实例绑定一个方法
stu = Student()
stu.name = 'kang'
print(stu.name)


def set_age(self, age):
	self.age = age
	pass

#给实例动态绑定一个方法  但是其他实例不会起作用
from types import MethodType
stu.set_age = MethodType(set_age, stu)
stu.set_age(23)
print(stu.age)

#如果要让其他实例也有作用，给类绑定方法



def set_name(self, name):
	self.name = name
	pass

Student.set_name = set_name

stu.set_name('k')

stu2 = Student()
stu2.set_name('b')
print(stu2.set_name)


#为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性