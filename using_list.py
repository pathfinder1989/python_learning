#!/usr/bin/python
#filename: using_list.py


fruitlist=['apple', 'bannan', 'mango']



print 'i have', len(fruitlist), 'fruit items'

print 'these are'

for i in fruitlist:
	print i,


fruitlist.append('grape')

print 'list are', fruitlist ,'after append'

fruitlist.sort()

print 'list are', fruitlist ,'after sort'

print 'the first is', fruitlist[0]

old = fruitlist[0]

del fruitlist[0]

print 'the old', old

print 'list now is', fruitlist