#!/usr/bin/env python
# Dumb interview Questions :)
# Find the first unique char in a string (from left to right)
def ustr(n):
    matches = {}
    for i in list(n):
        if i in matches.keys():
            matches[i] += 1
        else:
            matches[i] = 1
    return n[(min(map(lambda x: n.index(x), [i for i in matches.keys() if matches[i] == 1])))]
