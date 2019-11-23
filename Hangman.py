import random
number = random.randrange(0, 10)

words = ("table", "lunch", "seat", "bed", "drinks", "computer", "reading", "cake", "blue", "brown")

print (words)

word = (words[number])

blanks = (len(word) * "_")

print (len(word) * "_")

print ("Guess a letter or the whole word")

tries = 0

correct = 0

while tries < 8:
    guess = input()
    if guess == word:
        print ("WOW")
        break
    elif -1 != word.find(guess):
        if len(guess) == 1:
            if tries < 8:
                correct = correct + 1
                if correct == len(word):
                    print("Well Done!")
                    break
                if correct < len(word):
                    find_result = word.find(guess)
                    blanks = blanks.replace(blanks[(find_result)], guess, 1)
                    print (blanks)
                    print ("insane")
                    print ("Guess another letter or the word")
        else:
            print ("Write only one letter or guess the whole letter")
    elif -1 == word.find(guess):
        tries = tries + 1
        if tries == 8:
                print ("Better luck next time")
        print("You have " + str(8 - tries) + " tries left")
    elif len(guess >1 and guess <len(word)):
        print("guess only one letter or the whole word")
