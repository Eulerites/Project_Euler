#!/usr/bin/python

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

import sys

NUMBER = int(sys.argv[1])
remainder = NUMBER
current_largest_prime = 1

number_to_test = 2
while number_to_test <= remainder:
	while remainder % number_to_test is 0:
		current_largest_prime = number_to_test
		remainder = remainder / number_to_test
	number_to_test += 1

print 'largest prime factor of %s is %s' % (NUMBER, current_largest_prime)

