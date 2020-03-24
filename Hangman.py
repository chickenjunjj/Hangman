import random
class Hangman():
    def __init__(self):
        self.start()

    def start(self):
        print("[p] play")
        print("[q] quit")
        command = input()
        print("")
        if command == 'p':
            self.play()
        elif command == 'q':
            pass
        else:
            print("Invalid command \n")
            self.start()

    def play(self):
        guess_list = []
        number = random.randrange(0, 10) 
        words = ["table", "lunch", "seat", "bed", "drinks", "computer", "reading", "cake", "blue", "brown"]
        word = (words[number])
        blanks = (len(word) * "_")
        print (blanks)
        tries = 0
        correct = 0
        while tries < 8:
            print ("Guess a letter or the whole word \n")
            guess = input()
            indicies = self.find_indicies(guess, word)

            
            if len(guess) > 1:
                if guess == word:
                    print("You win! \n")
                    break
                else:
                    print("You lose \n")
                    break
            elif len(guess) == 1:
                if guess in guess_list:
                    print("Already guessed letter")
                elif len(indicies) > 0:
                    guess_list.append(guess)
                    correct = correct + 1
                    blanks = self.replace_str(blanks, indicies, guess)
                    print("")
                    print (blanks + "\n")
                    if correct == len(word):
                        print("You win! \n")
                        break
                    elif correct < len(word):
                        print("")
                        print ("Insane")
                else:
                    guess_list.append(guess)
                    print("Wrong answer")
                    tries = tries + 1
                    print("You have " + str(8 - tries) + " tries left \n")
                    if tries == 8:
                        print("You lose \n")
                        break
        self.start()
                
    def find_indicies(self, guess, word):
        num = 0
        indicies_list = []
        for letter in word:
            if guess == letter:
                indicies_list.append(num)
            else:
                pass
            num = num + 1
        return indicies_list
            

    def replace_str(self, text, indicies, replacement):
        for index in indicies:
            text = "%s%s%s"%(text[:index], replacement, text[index + 1:])
        return text
    
    

hangman = Hangman()
