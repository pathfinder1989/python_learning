#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):

    #@property
    def score(self):
        return self._score

    #@score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60
print('s.score =', s.score)
# ValueError: score must between 0 ~ 100!
s.score = 9999


#有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢


