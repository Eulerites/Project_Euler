#!/usr/bin/python

#storees the two previous fibs in a and b
#if even, adds the current fib into our sum

a = 1
b = 1
sum = 0
while b <= 4000000:
	c = a + b
	a = b
	b = c
	if b % 2 == 0:
		sum += b
print sum
