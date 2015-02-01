#!/usr/bin/python

results = [0,0]

def collatz(n):
    turns = 0
    while n > 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        turns += 1
    return turns
        
for i in range(1,1000000):
    if collatz(i) > results[1]:
        results = [i, collatz(i)]
print results
