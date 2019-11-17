#!/usr/bin/env python3
# Solved using a hashmap of letter => indexes of letter
# then finding the first palindrome between the two widest points
# decreasing width on each miss
from collections import defaultdict

def longest_palindromic_substring(s):
    longest = s[0]
    idx = 0
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
                    l = p[lo]
                    h = p[hi]+1
                    if s[l:h] == s[l:h][::-1] and len(s[l:h]) > 1:
                        if len(s[l:h]) > len(longest):
                            longest = s[l:h]
                            idx = l
                        elif len(s[l:h]) == len(longest):
                        # Since dict is unordered, if we have multiple
                        # matches of the same length, use the one with the
                        # lowest starting index (left-most)
                            if l < idx:
                                longest = s[l:h]
                                idx = l
                    hi -= 1
                hi = len(p) - 1
                lo += 1
    return longest
