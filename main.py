import random
from utils import clear_screen
from hangman_words import word_list
from hangman_art import logo, stages


def get_word():
    return random.choice(word_list)


def hangman():
    chosen_word = get_word()
    word_length = len(chosen_word)

    end_of_game = False
    lives = 6

    # Create blanks
    display = []
    for _ in range(word_length):
        display += "_"

    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        clear_screen()

        if guess in display:
            print("You've already guessed " + guess)
        # Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        # Check if user is wrong.
        if guess not in chosen_word:
            print(f"You guessed {guess} which is not in the word. You lose a life")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print(f"The answer is {chosen_word}. You lose.")

        # Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")

        # Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print("You win.")

        print(stages[lives])


if __name__ == '__main__':
    print(logo)
    hangman()
