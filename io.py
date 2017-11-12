
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

f = open('/Users/meishi/workspace_py/python_learning/animal.py', 'r')
str = f.read()
f.close()
print(str)


print('(----------------------------)')

with open('/Users/meishi/workspace_py/python_learning/animal.py') as f2
print(f2.read())