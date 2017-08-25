# _*_coding: utf-8 _*_
# 备份文件的操作 注释参见第四个

import os
import time

#需要备份的文件目录
source = ['/Users/meishi/workspace_py/python_learning']

target_dir = '/Users/meishi/workspace_py/'

today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')


if not os.path.exists(today):
	os.mkdir(today)
	print 'success create directory'

target = today + os.sep + now + '.zip'

zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

if os.system(zip_command) == 0:
	print 'successful backup to'
else:
	print 'backup failed'