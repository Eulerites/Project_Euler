#!/usr/bin/python

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


# this basically just builds a factor tree
# it stops after it hits a non prime or when it's iterated over half the goal
def primes():
    goal = 600851475143
    factors = []
    factor = 3.0
    if goal % 2.0 == 0: factors = [2]
    while factor * factor <= goal:
        if goal % factor == 0:
            for i in factors:
                if factor / i % 1 == 0:
                    return factors
            factors.append(int(factor))
        factor += 2
    if goal / factors[-1] % 1 == 0 : factors.append(goal / factors[-1])
    return factors
print primes()[-1]