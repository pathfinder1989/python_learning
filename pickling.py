# _*_coding: utf-8 _*_
#储存器什么玩意

import cPickle as p

shoplistfile = 'shoplist.data'

shoplist = ['apple', 'mango', 'carrot']

#写模式打开文件
f = file(shoplistfile, 'w')
#然后把list储存到文件中
p.dump(shoplist, f)
f.close()

#删除列表
del shoplist
#打开文件 取出储存的东西
f = file(shoplistfile)
storedlist = p.load(f)
print storedlist