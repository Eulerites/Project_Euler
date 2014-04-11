#!/usr/bin/env python

current = 1
previous = 1
total = 1

while current < 4000000:
    current = current + previous
    previous = current - previous
    if previous %2 == 0:
        total += previous

print total
