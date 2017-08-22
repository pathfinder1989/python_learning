#!/usr/bin/python
# Filename : while.py

number = 23
running = True

while  running:
	guess = int(raw_input('enter an integer : '))
	if guess == number:
		print 'congratulations, you guessed it'
		running = False
	elif guess < number:
		print 'higher'
	else:
		print 'lower'
else:
	print 'the while loop is over'
print 'done'