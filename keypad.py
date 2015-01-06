#!/usr/bin/env python
import time
from subprocess import call

integers = []
numbers = raw_input("Please enter a phone number:")
keypad = {
  0 : '',
  1 : '',
  2 : ['a', 'b', 'c'],
  3 : ['d', 'e', 'f'],
  4 : ['g', 'h', 'i'],
  5 : ['j', 'k', 'l'],
  6 : ['m', 'n', 'o'],
  7 : ['p', 'q', 'r', 's'],
  8 : ['t', 'u', 'v'],
  9 : ['w', 'x', 'y', 'z']
  }


for num in list(numbers):
  if num.isdigit() and not ( num == '0' or num == '1'):
    integers.append(int(num))

del numbers

integers = sorted(integers)

def main():
    print "using %s " % (integers)
    with open('/usr/share/dict/words', 'r') as d:
      for word in d.readlines():
        SortWord = sorted(word.rstrip())
        match = []
        if len(integers) == len(SortWord):
          for Index, Digit in enumerate(integers):
            if SortWord[Index].lower() in keypad[Digit]:
                match.append(SortWord[Index])
                if match == SortWord:
                  print "Match found!\t%s" % (word)
            else:
              break
main()
