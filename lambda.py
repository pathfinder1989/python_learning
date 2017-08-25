# _*_coding: utf-8 _*_
#文件读写操作

def make_repeater(n):
	return lambda s: s*n

twice = make_repeater(2)

print twice('word')
print twice(5)

