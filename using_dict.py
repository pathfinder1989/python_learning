# _*_coding: utf-8 _*_
#字典的使用

#实例化一个字典
dict = {
	'a' : 'a1',
	'b' : 'b1',
	'c' : 'c1',
	'd' : 'd1'
}

#打印这个字典，并打印字典的某一个key对应的值
print 'this dict is' , dict
print 'zhege dict de di key zhi shi %s' % dict["a"]

#修改某一个key对应的值

dict["a"] = 'a1'
print 'this dict is' , dict

#删除某一个key对应的值
del dict['a']
print 'this dict is' , dict


#打印字典所有的key和值
for key ,value in dict.items():
	print 'key: %s  value: %s \n' % (key, value)