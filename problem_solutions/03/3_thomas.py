#!/usr/bin/python

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


def primes(goal):
    factors = []
    factor = 2.0

    while factor <= goal:
        if goal % factor == 0:
            goal /= factor
            factors.append(int(factor))
        factor += 1
    return factors

print primes(600851475143)