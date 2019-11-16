#!/usr/bin/env python3
# Solved using a hashmap of letter => indexes of letter
# then finding the first palindrome between the two widest points
# decreasing width on each miss
from collections import defaultdict
def lps(s):
    pals = []
    pairs = defaultdict(list)
    for i in range(len(s)):
        pairs[s[i]].append(i)
    for pair in pairs:
        p = pairs[pair]
        if len(p) > 1:
            lo = 0
            hi = len(p) - 1
            while lo < len(p):
                while hi > lo:
                    if s[p[lo]:p[hi]+1] == s[p[lo]:p[hi]+1][::-1] and len(s[p[lo]:p[hi]+1][::-1]) > 1:
                        pals.append(s[p[lo]:p[hi]+1])
                    hi -= 1
                hi = len(p) - 1
                lo += 1
    return max(pals, key=lambda x: len(x))
