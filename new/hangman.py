import random
scramble_words=['array','list','python','java','tuple','set']
def choose_word():
    return random.choice(scramble_words).lower()
def draw_hangman(tries):

    if guess == 0:

      print( "________      ")

      print( "|      |      ")

      print( "|             ")

      print( "|             ")

      print( "|             ")

      print( "|             ")

    elif guess == 1:

      print( "________      ")

      print( "|      |      ")

      print( "|      0      ")

      print( "|             ")

      print( "|             ")

      print( "|             ")

    elif guess == 2:

      print( "________      ")

      print( "|      |      ")

      print( "|      0      ")

      print( "|     /       ")

      print( "|             ")

      print( "|             ")

    elif guess == 3:

      print( "________      ")

      print( "|      |      ")

      print( "|      0      ")

      print( "|     /|      ")

      print( "|             ")

      print( "|             ")

    elif guess == 4:

      print( "________      ")

      print( "|      |      ")

      print( "|      0      ")

      print( "|     /|\     ")

      print( "|             ")

      print( "|             ")

    elif guess == 5:

      print( "________      ")

      print( "|      |      ")

      print( "|      0      ")

      print( "|     /|\     ")

      print( "|     /       ")

      print( "|             ")

    else:

      print( "________      ")

      print( "|      |      ")

      print( "|      0      ")

      print( "|     /|\     ")

      print("|     / \     ")

      print( "|             ")

      print( "GAME OVER!")
def hangman():
    word_to_guess = choose_word()
    guessed_letters = set()
    tries = 6
    while tries > 0:
        display_word = ''.join(letter if letter in guessed_letters else '_' for letter in word_to_guess)
        print('Word:', display_word)
        print('guess left:', tries)
        if display_word == word_to_guess:
            print('correct word:', word_to_guess)
            return
        guess = input('Enter a letter: ').lower()

        if guess in guessed_letters:
            print('letter already guessed!')
        elif guess.isalpha() and len(tries) == 1:
            guessed_letters.add(guess)
            if guess not in word_to_guess:
                tries -= 1
        else:
            print('Incorrect guess. enter letter.')

        
        display_hangman(6 - tries)
    
    print('ranout of chances:', word_to_guess)
        
hangman()  
