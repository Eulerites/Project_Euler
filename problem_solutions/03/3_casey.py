#!/usr/bin/python

def primes(goal):
        factors = [2]
        factor = 3
        while goal % 2 == 0:
                goal /= 2

        while goal > 1:
                if goal % factor == 0:
                        goal /= factor
                        factors.append(factor)
                factor += 2
        return factors[-1]

print primes(600851475143)
