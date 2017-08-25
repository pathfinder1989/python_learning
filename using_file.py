# _*_coding: utf-8 _*_
#文件读写操作

poem = '''\
是不是要把这个字符串写到文件里面去啊 
应该就是要把这一句写到文件
python读写呗 来自文件using_file.py
'''

#w就是writing的意思呗
f = file('test.txt', 'w')
f.write(poem)
f.close

f = file('test.txt')
#循环逐行读取打印
while True:
	line = f.readline()
	if len(line) == 0:
		break
	print line,

f.close()