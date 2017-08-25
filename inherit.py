# _*_coding: utf-8 _*_
#!/usr/bin/python
#主要演示继承的使用

class SchoolMember(object):
    """docstring for ClassName"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def tell(self):
        print 'tell me your name is %s age is %s' % (self.name, self.age)


#python的继承方式是这个样子的
class Teacher(SchoolMember):
    """docstring for Teacher

        detail text"""

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print 'init teacher name : %s' % self.name

    def tell (self):
        SchoolMember.tell(self)
        print 'salary is : %s' %  self.salary 

class  Student(SchoolMember):
    """docstring for  Student"""
    def __init__(self, name, age, marks):
        #这儿不能用super必须用继承的那个类
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print 'init student name: %s' % self.name

    def tell(self):
        SchoolMember.tell(self)
        print 'Marks: "%s"' % self.marks


t = Teacher('laoshi', 40, '2w')
s = Student('xuesheng', 18, '98分')

print 

members = [t, s]
for member in members:
    member.tell()