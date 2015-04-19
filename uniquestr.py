#!/usr/bin/env python
# Dumb interview Questions :)
# Find the first unique char in a string (from left to right)
import timeit

def ustr(n):
    matches = {}
    for i in list(n):
        if i in matches.keys():
            matches[i] += 1
        else:
            matches[i] = 1
    return n[(min(map(lambda x: n.index(x), [i for i in matches.keys() if matches[i] == 1])))]

# Better Algo
def ustring(s):
    slist = list(s)
    for i in slist:
        if i in slist[slist.index(i) + 1::]:
            next
        else:
            return i


timeit.timeit("ustr('pzaramoumpteruotle')",setup="from __main__ import ustr")
timeit.timeit("ustr('pzaramoumpteruotle')",setup="from __main__ import ustr" )
timeit.timeit("ustr('pzaramoumpteruotle')", setup="from __main__ import ustr" )
timeit.timeit("ustring('pzaramoumpteruotle')",setup="from __main__ import  ustring")
timeit.timeit("ustring('pzaramoumpteruotle')",setup="from __main__ import ustring" )
timeit.timeit("ustring('pzaramoumpteruotle')",setup="from __main__ import ustring" )

