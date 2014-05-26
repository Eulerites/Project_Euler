#!/usr/bin/python

primeList = [2]
index = 1
while len(primeList)<= 10000:
	index += 2
	prime = True
	for x in primeList:
		if index % x == 0:
			prime = False
			break
	if prime:
		primeList.append(index)
print primeList[-1]
