#Iterate through every instance from 0 to 999
#summing all integers factorable by 3, or 5

sum = 0

for i in xrange(0,1000):
        if i % 3 == 0 or i % 5 == 0:
                sum += i

print sum
