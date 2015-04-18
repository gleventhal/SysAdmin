#!/usr/bin/env python
import os
import re
import sys
def matchedParens(pstring):
    if not isinstance(pstring, list):
        if isinstance(pstring, str):
            pstring = list(pstring)
        else:
            print "Usage: %s(list or string)" % os.path.basename(__file__)
            return False
    if pstring.count('(') != pstring.count(')') or pstring[0] == ')' or pstring[-1] == '('\
    or re.findall(r'[^\(\)]', ''.join(pstring)):
        print "Base case failed"
        return False
    matched = []
    open = False
    while len(matched) < len(pstring):
        for i in range(len(pstring)):
            if i in matched:
                next
            if open == False and pstring[i] == '(':
                matched.append(i)
                open = True
                next
            elif open == False and pstring[i] == ')':
                print "No opened paren and finding a closed"
                return False
            elif open == True and pstring[i] == '(':
                next
            elif open == True and pstring[i] == ')':
                matched.append(i)
                open = False
                break 
            else:
                print "Unexpected Result"
                return False
    return True

print matchedParens(sys.argv[1])
#print matchedParens('((()))()(())')
#print matchedParens('(((())))()()(()')
#print matchedParens('(((())))()()()()')
#print matchedParens('((((){)))()()()()')
#print matchedParens(pstring=1234)
#
