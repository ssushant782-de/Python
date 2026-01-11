import random

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.
word_list=["California","Texas","Florida"]
chosen_word= list(random.choice(word_list).lower())
length = len(chosen_word)
guessing_word = len(chosen_word) * "_"
guessing_word_list = list(len(chosen_word) * "_")
#print(len(guessing_word))
print(f"Computer Chosen word: {guessing_word}")
print(chosen_word)
total_lives = 5
while total_lives > 0 and guessing_word_list != chosen_word:
    guessed_letter = input("Guess a letter: ").lower()
    if guessed_letter in chosen_word:
        for index in range(length):
            #index = chosen_word.index(guessed_letter)
            #print(index)
            if chosen_word[index]==guessed_letter:
                guessing_word_list[index] = guessed_letter
                guessing_word = "".join(guessing_word_list)
                print(guessing_word)
    else:
        total_lives-=1
        print(f"that's a wrong guess.. Hangman is left with {total_lives} lives")
if total_lives == 0:
    print("Hangman died because of your inefficiency!!")
elif guessing_word_list == chosen_word:
    print("You saved the hangman!! Hooray!!")