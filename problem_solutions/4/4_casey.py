#!/usr/bin/python

#returns a palindrome of the passed int
def palindromize(number):
	number = list(str(number))
	index = len(number)
	while index > 0:
		index -= 1
		number.append(number[index])
	return int(''.join(number))

#returns if the palendrome is factorable by two three digit ints
def factorable(palen):
	divisor = 999
	while divisor >= 100:
		if palen / divisor < 1000 and  palen % divisor == 0:
			print palen
			return True
		else:
			divisor -= 1
	return False

x = 999
while x > 99:
	if factorable(palindromize(x)):
		break
	else:
		x-=1

