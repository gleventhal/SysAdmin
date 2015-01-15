#!/usr/bin/env python
dictionary = '/usr/share/dict/words'
integers = [int(num) for num in sorted(raw_input("Please enter a phone number:")) if num.isdigit() and not (num == '0' or num == '1') ]
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

def checkWord(word):
    if len(integers) == len(word.rstrip()):
      SortWord = sorted(word.rstrip())
      count = 1
      for Index, Digit in enumerate(integers):
        if SortWord[Index].lower() in keypad[Digit]:
          count += 1
      return count == len(word)
    else:
      return False

with open(dictionary, 'r') as d:
  for word in d.readlines():
    if checkWord(word):
      print word
