#!/usr/bin/python

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def primes():
    goal = 600851475143
    factors = []
    factor = 3.0
    while factor * factor <= goal:
        if goal % factor == 0:
            for i in factors:
                x = factor / i
                if x % i % 1 == 0:
                    return factors
            factors.append(int(factor))
        factor += 2
    print factors
print primes()[-1]