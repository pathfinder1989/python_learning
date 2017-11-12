#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO
f = StringIO()
f.write('hello')
print(f.getvalue())


from io import StringIO
f = StringIO('this is hello world')
while True:
	s = f.readline()
	if s == '':
		break
	print(s.strip())