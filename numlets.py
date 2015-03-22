#!/usr/bin/env python
# Project Euler Problem 17

letters = 0
nums = {
  0 : '',
  1 : 'one',
  2 : 'two',
  3 : 'three',
  4 : 'four',
  5 : 'five',
  6 : 'six',
  7 : 'seven',
  8 : 'eight',
  9 : 'nine',
  10: 'ten',
  11: 'eleven',
  12: 'twelve',
  13: 'thirteen',
  14: 'fourteen',
  15: 'fifteen',
  16: 'sixteen',
  17: 'seventeen',
  18: 'eighteen',
  19: 'nineteen',
  20: 'twenty',
  30: 'thirty',
  40: 'forty',
  50: 'fifty',
  60: 'sixty',
  70: 'seventy',
  80: 'eighty',
  90: 'ninety',
  100: 'one hundred',
  1000: 'one thousand'
}

for i in range(1,1001):
    if i in nums:
        letters += len(nums[i].replace(' ', ''))
    else:
        if len(str(i)) == 4:
            letters += len(nums[str(i)[0]] + 'thousand')
        elif len(str(i)) == 3:
            one   = int(str(i)[0])
            if int(str(i)[1]) != 0 and int(str(i)[1:]) in nums.keys():
                two = nums[int(str(i)[1:])]
                three = ''
            else:
                two   = int(str(i)[1])
                three = int(str(i)[2])
                if two == 0:
                    two = ''
                else: 
                    two = str(nums[two * 10])
                if three == 0:
                    three = ''
                else:
                    three = nums[int(three)]
                if two != '' or three != '':
                    middle = 'hundredand'
                else:
                    middle = 'hundred'
            letters += len(str(nums[one]) + middle + two + three) 
        elif len(str(i)) == 2:
            res = nums[int(str(i)[0]+'0')] + nums[int(str(i)[1])]
            letters += len(res)      
print letters
