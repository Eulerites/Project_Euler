#!/usr/bin/python

def leastCommonProduct(number):
	product = 1
	primes = [2]
	for x in xrange(3,number+1):
		prime = True
		for y in primes:
			if x % y == 0:
				prime = False
				break
		if prime:
			primes.append(x)
	for x in primes:
		index = 1
		while x**(index+1) < number:
			index += 1
		product *= x**index
	print product

leastCommonProduct(20)
