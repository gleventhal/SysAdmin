#!/usr/bin/python
# Words With Enemies
# Reddit /r/dailyprogrammer challenges

import sys, re

left = sys.argv[1]
right = sys.argv[2]

def CompareWords(left, right):
    '''Test the two words, removing any duplicate letters'''
    lleft=list(left)
    lright=list(right)
    dupes=[]
    right_matched_indexes=[]
    print "Comparing %s with %s" % (left, right)
    for li,l in enumerate(lleft):
        for ri,r in enumerate(lright):
            if l == r and ri not in right_matched_indexes:
                dupes.append(l)
                right_matched_indexes.append(ri)
                break
                
    for d in dupes:
        left=re.sub(d, '', left, 1) 
        right=re.sub(d, '', right, 1)          
    if len(left) > len(right):
        return 'Left wins with %s' % (left)
    elif len(right) > len(left):
        return 'Right wins with %s' % (right)
    else:
        return 'Tie!!'
                
print CompareWords(left, right)
