# _*_coding: utf-8 _*_
#tuple in tuple

tuple1 = ('t1', 't2', 't3', 't4')
print 'this tuple is', tuple1
print 'this tuple length is ', len(tuple1)

#元组套元组
newtuple = ('n1', 'n2', tuple1)

print 'this2 tuple is', newtuple
print 'this2 tuple length is ', len(newtuple)


print '元组套元组',newtuple[2][2]