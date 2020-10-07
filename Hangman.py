import random
import string

print(' '.join(['H', 'A', 'N', 'G', 'M', 'A', 'N']))


def play():
    wordList = ['python', 'java', 'kotlin', 'javascript']
    randomWords = random.choice(wordList)
    matchwords = ['-' for _ in randomWords]
    words = frozenset(randomWords)
    guessed = set()
    doubleguessed = set()
    count = 8
    while count > 0:
        print('\n', ''.join(matchwords))
        guess = input('Input a letter: ')
        if guess not in string.ascii_lowercase and len(guess) < 2:
            print("It is not an ASCII lowercase letter")
            continue

        if len(guess) != 1:
            print('You should input a single letter')
            continue

        if guess in doubleguessed:
            print("You already typed this letter")
            continue

        doubleguessed.add(guess)

        if guess not in guessed:
            if guess in words:
                for i, j in enumerate(randomWords):
                    if guess == j:
                        matchwords[i] = guess
                        guessed.add(guess)
                if guessed == words:
                    print('You guessed the word {0}!\nYou survived!\n'.format(randomWords))
                    break
            else:
                print('''No such letter in the word''')
                count -= 1
    else:
        print('You lost!', '\n')


while True:
    userWish = input('Type "play" to play the game, "exit" to quit: ')
    print()
    if userWish.lower() == 'play':
        play()
    elif userWish.lower() == 'exit':
        break
