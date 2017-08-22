#!/usr/bin/python
# Filename: using_sys.py

import sys

print 'the command line arguments are: '
for i in sys.argv:
	print i

print '\n\n the pythonpath is', sys.path, '\n'