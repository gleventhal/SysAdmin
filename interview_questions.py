#!/usr/bin/python

def findsum(a, n):
  ''' Find whether a consecutive array slice sums up to n '''
  for i in range(len(a)):
    j = i + 1
    while j <= len(a):
      if sum(a[i:j]) == n:
        return True
      j += 1
  return False

def nonzero(a):
  ''' given an array of ints, push all zeros to the end '''
  zeros = [0 for i in range(a.count(0))]
  x = [ i for i in a if i != 0]
  x.extend(zeros)
  return(x)

def egg_drop(n):
    ''' Find the highest floor in a building that an egg can drop from without breaking '''
    t = [1,11]
    while t[0] < 100:
        if t[1] >= n: 
            print 'break_an_egg on floor %d' % t[1] 
            for i in range(t[0],t[1]):
                if i >= n:
                    print  'break_an_egg on floor %d' % i 
                    return i - 1
        else:
            t[0] += 10
            t[1] += 10
    return(100)

def sum_to_zero(a):
  ''' given an array of ints, find 3 elements that sum to 0 '''
  for i in a:
    for j in a[1:]:
      for k in a[2:]:
        if i + j + k == 0:
          return (i,j,k)

