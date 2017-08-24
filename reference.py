# _*_coding: utf-8 _*_

print '----------------------'
list = ['1','2','3','4']
#这只是对象的引用
newlist = list
del list[0]

print 'list is', list
print 'newlist is', newlist

# 相当于copy
anotherlist = list[:]
print 'anotherlist is', anotherlist

print '----------------------'

del anotherlist[0]

print '----------------------'
print 'list is', list
print 'anotherlist is', anotherlist
print '----------------------'