import random

# Constant
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
    ===''','''
  +---+
  0   |
      |
      |
    ===''','''
  +---+
  0   |
  |   |
      |
    ===''','''
  +---+
  0   |
 /|   |
      |
    ===''','''
  +---+
  0   |
 /|\  |
      |
    ===''','''
  +---+
  0   |
 /|\  |
 /    |
    ===''','''
  +---+
  0   |
 /|\  |
 / \  |
    ===''', '''
  +---+
 [O   |
 /|\  |
 / \  |
    ===''', '''
  +---+
 [O]  |
 /|\  |
 / \  |
    ===''']


WORDS = {'Colors':'red orange yellow green blue indigo violet white black brown'.split(),
         'Shapes':'square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon hexagon septagon octagon'.split(),
         'Fruits':'apple orange lemon lime pear watermelon grape grapefruit cherry banana cantaloupe mango strawberry tomato'.split(),
         'Animals':'bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep skunk squid tiger turkey turtle weasel whale wolf wombat zebra'.split()}





def get_random_word(wordDict):
    #This fuction returns a random string from the passed dictionary of lists of strings and its key
    #First, randomly select a key from its dictionary

    wordKey = random.choice(list(wordDict.keys()))
    #Second, randomly select a word from the key's list in the dictionary
    word_index = random.randint(0, len(wordDict[wordKey]) - 1)

    #print([wordDict[wordKey][word_index], wordKey]) #prints out a list
    return [wordDict[wordKey][word_index], wordKey]#this should return a word from the list that we got from the dictionry

def print_board(missed_letters, correct_letters, secret_word): #
    print(HANGMAN_PICS[len(missed_letters)])
    print()
    print("Missed letters: ")
    for letter in missed_letters:
        print(letter, end="")
    print()
    blanks = "_" * len(secret_word)
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]
    for letter in blanks:
        print(letter + " ", end="")
    print()

def get_guess(already_guessed):
    while True:
        print("Guess a letter:")
        guess = input().lower()
        if len(guess) != 1:
            print("Please guess a single letter at a time.")
        elif guess in already_guessed:
            print("You have already guessed that letter. Try again.")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("That is not a letter. Try again.")
        else:
            return guess

def play_again():
    print("Do you want to play again? (yes or no)")
    return input().lower().startswith("y")




def play_game():
    print("H A N G M A N")
    print("A game by Late'jah Whittaker")

    difficulty = ''
    #while difficulty not in 'EMH':
    print('Enter difficulty: E - Easy, M - Medium, H - Hard')

    difficulty = input().upper()
    if difficulty == 'M':
        del HANGMAN_PICS[8]
        del HANGMAN_PICS[7]
    if difficulty == 'H':
        del HANGMAN_PICS[8]
        del HANGMAN_PICS[7]
        del HANGMAN_PICS[5]
        del HANGMAN_PICS[3]
    
    missed_letters, correct_letters = '', ''
    secret_word, secretSet = get_random_word(WORDS)
    stop_game = False
    games_played = 0 #added this
    games_won = 0 #added this
    games_lost = 0 #added this


    while not stop_game:
        print('The secret word is in the set: ' + secretSet)
        print_board(missed_letters, correct_letters, secret_word)
        guess = get_guess(missed_letters + correct_letters)
        if guess in secret_word:
            correct_letters += guess
        else:
            missed_letters += guess
        # check if player has won
        # To do so, you need to compare what they've guessed to the secret word
        # Essentially, check if all the letters in secret_word are in correct_letters
        i = 0
        match = True
        while match and i < len(secret_word):
            if secret_word[i] not in correct_letters:
                match = False
            i += 1
        if match:
            print("Yes! The secret word is " + secret_word + "! You win!")
            games_won += 1 #added this
            games_played += 1 #added this
            stop_game = True
        elif len(missed_letters) == len(HANGMAN_PICS)-1: #Added the -1 to the lenght of the Hangman Pics
            print_board(missed_letters, correct_letters, secret_word)
            games_played += 1 #added this
            games_lost += 1 #added this
            print("You have run out of guesses!\nAfter " +
                  str(len(missed_letters)) + " missed guesses and " +
                  str(len(correct_letters)) + " correct guesses, " +
                  "the word was \"" + secret_word + "\"")
            stop_game = True
        if stop_game:
            print("You have played ", games_played, "games.") #added this
            print("You have won", games_won, "games and you have lost", games_lost, "games") #added this
            if play_again():
                missed_letters, correct_letters = "", ""
                stop_game = False
                secret_word, secretSet = get_random_word(WORDS)

            else:
                print("Goodbye!")

play_game()
