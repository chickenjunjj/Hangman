import random
number = random.randrange(0, 5)

words = ["Yoshito", "Kai", "Ryo", "Kazuki", "Daniel"]

word = (words[number])

print (len(word) * "_")

print (word)

print ("Guess a letter or the whole word")

tries = 0

while tries < 8:
    guess = input()
    if guess == word:
        print ("WOW")
        break
    elif -1 != word.find(guess):
        if len(guess) == 1:
            print ("insane")
            tries = tries + 1
            if tries < 8:
                print ("Guess another letter or the word")
        else:
            print ("Write only one letter or guess the whole letter")
