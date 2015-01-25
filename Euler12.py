#!/usr/bin/python

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

nums = [1]
i = 1

while len(factors(sum(nums))) < 500:
    i = i+1
    nums.append(i)
print sum(nums)
