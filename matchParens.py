#!/usr/bin/env python3
# For Felix

def matchParens(pstring):
    '''Check string of parenthesis for sane groupuing and nesting'''
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

# Check Function
assert matchParens('((()))') == True
assert matchParens('(()(())())') == True
assert matchParens('()()(') == False
assert matchParens('(()(())()') == False
assert matchParens('(()())()((()))') == True

def elementMatch(a1, a2):
    '''Find first similar element in a pair of sorted arrays'''
    try:
        return sorted(set(a1) & set(a2))[0]
    except IndexError:
        return False

# Check function
assert elementMatch([2, 3, 5, 7, 8, 23], [4, 6, 8, 15, 23, 34]) == 8
assert elementMatch([12, 13, 25, 27, 28, 123], [24, 26, 28, 215, 123, 134]) == 28
assert elementMatch([12, 13, 25, 27, 28, 223], [124, 126, 128, 215, 123, 134]) == False # No Match
