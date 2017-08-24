# _*_coding: utf-8 _*_
#!/usr/bin/python
# Filename: seq.py 
# 序列的使用

shoplist = ['apple', 'mango', 'carrot', 'banana']

# Indexing or 'Subscription' operation
print 'Item 0 is', shoplist[0]
print 'Item 1 is', shoplist[1]
print 'Item 2 is', shoplist[2]
print 'Item 3 is', shoplist[3]
print 'Item -1 is', shoplist[-1]
print 'Item -2 is', shoplist[-2]

# Slicing on a list
#1 到 3 不包括3
print 'Item 1 to 3 is', shoplist[1:3]
#2 到 末尾 包含末尾
print 'Item 2 to end is', shoplist[2:]
#1 到 末尾 不包含末尾
print 'Item 1 to -1 is', shoplist[1:-1]
#全部
print 'Item start to end is', shoplist[:]

# Slicing on a string
name = 'swaroop'
print 'characters 1 to 3 is', name[1:3]
print 'characters 2 to end is', name[2:]
print 'characters 1 to -1 is', name[1:-1]
print 'characters start to end is', name[:]
