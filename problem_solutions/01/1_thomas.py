#!/usr/bin/env python

total = 0

for i in xrange(0,1000):
    if i % 3 == 0 or i % 5 == 0:
        total += i

print total
