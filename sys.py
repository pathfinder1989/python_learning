#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#第1行和第2行是标准注释，第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，第2行注释表示.py文件本身使用标准UTF-8编码；

#表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
'a test module'

#使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名
__author__ = 'Michael jodan'


#类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用
import sys

def test():
	args = sys.argv
	if len(args) == 1:
		print('hello world')
	elif len(args)==2:
		print('Hello, %s!' % args[1])
	else:
		print('Too many arguments!')

if __name__=='__main__':
	test()