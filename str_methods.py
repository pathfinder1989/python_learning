# _*_coding: utf-8 _*_
#字符串在一门语言里总是一个特别的存在

myname = 'kangbo'

#以什么开头 前缀
if myname.startswith('a'):
	print '以a开头的字符串'
else:
	print '不是以a开头的字符串'


#字符串包含
a = 'an'
if a in myname:
	print '该字符串包含字母a'

b = 'o'

#这个会把索引打出来
print 'ldfsj---', myname.find(b)