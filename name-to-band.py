#!/usr/bin/python
import urllib2, re, sys, random

myName = raw_input('What is your name?')

listName = list(myName)
print 'trying %s' %  listName
for letter in listName:
    if letter != ' ':
        myURL = 'http://www.oldielyrics.com/%s.html' % letter.lower()
        r=urllib2.urlopen(myURL)
        band = random.choice(re.findall('>[A-Z ]{4,}<', r.read()))
        print re.sub(r'(<|>)', '**', band)
    else:
        print "\n"
