#!/usr/bin/python
#          	#
#   Hangman! 	#
#          	#
#################
import re, random, subprocess, time

file = '/usr/share/dict/words'
num_lines = sum(1 for line in open(file))
choice = random.randint(1, num_lines)
results = []
misses = []
win = [ '''
#############
# YOU WIN!! #
#############
''',
''
]

gallows = [ '''
	oooooo
	o     .
	o    . .
	o     .
	o
	o
	o
        |
    m===========m
''',
'''
        ooooo___
        o   (. .) 
        o    <  )
        o     0
        o
        o
        o
        |
    m===========m
''',
'''
        ooooo___
        o   (. .) 
        o    <  )
        o     0\\
        o     /
        o    /
        o
        |
    m===========m
''',
'''
        ooooo___
        o   (. .) 
        o    <  )
        o     0\\ 
        o     / \\ 
        o    /   \\ 
        o
        |
    m===========m
''',
'''
        ooooo___
        o   (. .) 
        o    <  )
        o     0\\
        o     /|\\
        o    / | \\
        o      |
        |
    m===========m
''',
'''
        ooooo___
        o   (. .) 
        o    <  )
        o     0\\
        o     /|\\
        o    / | \\
        o      |
        |   ===
    m===========m
''',
'''
        ooooo___
        o   (x x) 
        o    <  )
        o     0\\
        o     /|\\
        o    / | \\
        o      |
        |   === ===
    m===========m\n
    ############
    #Game Over!#
    ############\n\n
    You\'re hanged!
'''
]

def drawScreen(x=None):
    subprocess.call('clear')
    print "\t" + gallows[len(misses)]
    print "\n" + ' '.join(results) + '\n' * 2
    if misses:
        print "Incorrect guesses: %s" % (' '.join(misses))
    if ''.join(results) == word:
        dnull = open('/dev/null', 'w')
        f = subprocess.call(["which", "figlet"],stdout=dnull)
        if not f:
            subprocess.call(["figlet", "you win!"])
        else:
            print win[0]
        time.sleep(2)
        exit()
    if x == 'loss':
        print "The word was %s\n\n" % (word)
        time.sleep(2)
        exit(1)
    guess = raw_input("\nGuess a letter...\n")
    return guess

with open(file, 'r') as words:
    for i in range(choice):    
        word = words.readline().rstrip('\n')

letters = list(word)

for letter in range(len(word)):
    results.append('-')


def __main__():
    while ( len(misses) < 6):
        guess = drawScreen()
        if not guess.isalpha():
            print "Choose only lower case letters please!"
            guess = drawScreen()
        indices = [i for i, x in enumerate(letters) if x.lower() == guess.lower()]
        if indices:
            for i in indices:
                results[i] = guess
        else:
            print '\a'
            misses.append(guess)

__main__()
drawScreen(x='loss')
