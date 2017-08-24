# _*_coding: utf-8 _*_
# 备份文件的操作

import os
import time

#需要备份的文件目录
source = ['/Users/meishi/workspace_py/python_learning']

target_dir = '/Users/meishi/workspace_py/backup_test'

target = target_dir + time.strftime('%Y-%m-%d %H:%M:%S') + '.zip'

zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

if os.system(zip_command) == 0:
	print 'successful backup to'
else:
	print 'backup failed'