# _*_coding: utf-8 _*_
# 备份文件的操作

import os
import time

#需要备份的文件目录
source = ['/Users/meishi/workspace_py/python_learning']
#备份到的目标目录
target_dir = '/Users/meishi/workspace_py/'

today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

#备份注释
comment = raw_input('请输入这个备份的描述---> ：')
if len(comment) == 0:#没有输入备份描述，正常处理
	target = today + os.sep + now + '.zip'
else:#输入备份描述后，将描述的空格替换成下划线然后添加到文件名里
	target = today + os.sep + now + '_' + \
	comment.replace(' ', '_') + '.zip'

#如果今天没备份 创建今天的备份目录
if not os.path.exists(today):
	os.mkdir(today)
	print 'success create directory'
#zip压缩命令 
#-q不显示指令执行过程；
# -r：递归处理，将指定目录下的所有文件和子目录一并处理；

zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

if os.system(zip_command) == 0:
	print 'successful backup to'
else:
	print 'backup failed'