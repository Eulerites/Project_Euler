#!/usr/bin/python

a=1
b=1
c=1


def comparison():
	if (a**2 + b**2) == (c**2):
		print a*b*c
		exit

while a < 250:
	b = 500 - a
	while b < (1000 - a)/2:
		c = 1000 - a - b
		comparison()
		b += 1
	a += 1


