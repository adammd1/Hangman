import random
class Hangman():
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list).lower()
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
    def check_guess(self,guess):
        guess = guess.lower()
        if guess in self.word:
            print("Good guess! " + str(guess) + " is in the word.")
            n = 0
            for i in self.word:
                if i == guess:
                    self.word_guessed[n] = i
                n+=1
            self.num_letters -= 1
            print(self.word_guessed)
        else:
            self.num_lives -= 1
            print("Sorry, " + str(guess) + " is not in the word.")
            print("You have " + str(self.num_lives) + " lives left.")
    def ask_for_input(self):
        guess = str(input("Enter a single letter: "))
        if guess.isalpha() == False:
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            self.check_guess(guess)

def play_game(word_list):
    game = Hangman(word_list)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        if game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations!! You won!!")
            break
my_list = ["Grapes","Pineapple","Banana","Mango","Figs"]
play_game(my_list)
