#!/usr/bin/python
#                #
#   Hangman!     #
#                #
##################
import re, random, subprocess, time, sys

title = '''
 _   _                                         _ 
| | | | __ _ _ __   __ _ _ __ ___   __ _ _ __ | |
| |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \| |
|  _  | (_| | | | | (_| | | | | | | (_| | | | |_|
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_(_)
                   |___/                         
'''
file = '/usr/share/dict/words'
num_lines = sum(1 for line in open(file))
choice = random.randint(1, num_lines)
results = []
misses = []
gameOver = '''
##############
# Game Over! #
##############
'''
win = [ '''
#############
# YOU WIN!! #
#############
'''
]

with open(file, 'r') as words:
    for i in range(choice):    
        word = words.readline().rstrip('\n')
letters = list(word)
for letter in range(len(word)):
    results.append('-')

gallows = [ '''
        oooooo
        o     .
        o    . .
        o     .
        o
        o
        o
        |
        |
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
        |
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
        o   3
        |
        |
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
        o   3     M
        |
        |
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
        o   3  |  M
        |
        |
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
        o   3  |  M
        |     / 
        |   =/
        |
    m===========m
''',
'''
        ooooo___
        o   (x x) 
        o    <  )
        o     0\\
        o     /|\\
        o    / | \\
        o   3  |  M
        |     / \\
        |   =/   \\=
        |
    m===========m\n
'''
]

def playAgain():
    ans = raw_input('Play Again?\n(y/n):')
    if ans.lower() == 'y':
        cmd = [ 'python', sys.argv[0]]
        subprocess.call(cmd)
    elif ans.lower() == 'n':
        print "\n\n"
        exit(1)
    else:
        playAgain()

def drawScreen(x=None):
    subprocess.call('clear')
    print title
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
        playAgain()
    elif x == 'loss':
        dnull = open('/dev/null', 'w')
        f = subprocess.call(["which", "figlet"],stdout=dnull)
        if not f:
            subprocess.call(["figlet", "Game Over!"])
        else:
            print gameOver
        print "The word was %s\n\n" % (word)
        time.sleep(2)
        playAgain()
    else:
        guess = raw_input("**Guess a letter**\n")
        return guess

def __main__():
    while ( len(misses) < 6):
        guess = drawScreen()

        if guess == None or not guess.isalpha():
            print "Choose only lower case letters please!"
            time.sleep(2)
            guess = drawScreen()
       
        else:

            indices = [i for i, x in enumerate(letters) if x.lower() == guess.lower()]
            if indices:
                for i in indices:
                    results[i] = guess
            else:
                print '\a'
                misses.append(guess)


if __name__ == __main__():
    __main__()

drawScreen(x='loss')
