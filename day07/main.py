import random
import hangman_art, hangman_words

print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)


live = 6

print(f'Psst, the solution is {chosen_word}')


word_length = len(chosen_word)
display = []
End_of_game = False
for i in range(word_length):
    display.append("_")

while (End_of_game == False):

    guess = str(input("Guess a letter: ")).lower()

    
    if guess in display:
      print(f"You've already guessed the letter {guess}, please enter a new word")
      guess = str(input("Guess a letter: ")).lower()
   
    for position in range(word_length):
        letter = chosen_word[position]
       # print(f"Current position {position}\n Current letter: {letter} \n Guessed letter: {guess}")       
        if letter == guess:
            display[position] = letter

    print(f"{''.join(display)}")

    if guess not in chosen_word:
        if live == 0:
            End_of_game = True
            print("GAME OVER")
        else:
            print(f"The letter {guess} is not in the Word")
            live -= 1

    if "_" not in display:
        print('You win')
        End_of_game = True

    
    print(hangman_art.stages[live])