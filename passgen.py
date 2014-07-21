#!/usr/bin/python

# A Mediocre Password Generator

import random, string

plen  = random.randint(6,10)
lower = string.lowercase
upper = string.uppercase
nums  = range(10)

pword = []
for i in range(plen):
  if ((i + random.randint(0,100)) % 2 == 0):
    pword.append(lower[random.randint(0,len(lower) - 1)])
  elif ((i + random.randint(0,100)) % 3 == 0):
    pword.append(str(nums[random.randint(0,len(nums) - 1)]))
  else:
    pword.append(upper[random.randint(0,len(upper) - 1)])

p = ''.join(pword)
print("Password is {0}".format(p))
