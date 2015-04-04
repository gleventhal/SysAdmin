#!/usr/bin/env python3
# For Felix

def matchParens(pstring):
    plist = [l for l in pstring]
    newlist = []
    if plist[0] == ')' or plist.count('(') != plist.count(')') or plist[-1::] == '(':
        return False
    while len(plist) > 0:
        head, *tail = plist
        if head == '(':
            newlist.append(plist.pop(plist.index(head)))
            right = tail.index(')')
            if isinstance(right, int):
                newlist.append(plist.pop(right))
            else: 
                return False
        else:
            return False
    return True

assert matchParens('((()))') == True
assert matchParens('(()(())())') == True
assert matchParens('()()(') == False
assert matchParens('(()(())()') == False
