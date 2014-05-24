#!/usr/bin/python

primeSum = 2
primeList = [2]
index = 3
while primeList[-1]<2000000:
	prime = True
	for x in primeList:
		if index % x == 0:
			prime = False
			break
	if prime:
		primeList.append(index)
		primeSum += index
		print index
	index += 2	
print primeSum
