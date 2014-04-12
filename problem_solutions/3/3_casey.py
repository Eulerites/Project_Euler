#!/usr/bin/python
import math
primes = [2,3]
number = 600851475143
#Checks if prime in our growing list of primes
def isPrime(x):
	for i in primes:
		if x % i == 0:
			return False
	return True

#Adds the next prime number to our list
def nextPrime():
	nextNum = primes[-1]
	while 1==1:
		nextNum += 2
		if isPrime(nextNum):
			primes.append(nextNum)
			return

#finding the largets prime factor
while number % 2 ==0:
	number /= 2
while number >1:
	if number % primes[-1] == 0:
		number /= primes[-1]
	else:
		nextPrime()
print primes[-1]
