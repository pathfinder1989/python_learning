#!/usr/bin/python
# Filename : if.py

number = 23
guess = int(raw_input('Enter an integer : '))
if guess == number:
    print 'Congratulations, you guessed it.'
    #New block starts here
elif guess < number:
    print 'NO, it is a little higher than that'
    #Another block
    #you can do whatever you want in a block...
else:
	print 'No, it is a little lower than that'

print 'done'