import random
words = ['apple','strawberry','mango','banana']
chosen_word = random.choice(words)
word_display = ['_' for _ in chosen_word]
attempts = 5
print("Welcome to HANGMAN!!!!")
while attempts > 0 and '_' in word_display:
    print("\n" + ' '.join(word_display) )
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess
        attempts -= 1
        print("Attempts left: " + str(attempts))
    else:
        print("Sorry, that's wrong. Try again")
        attempts -= 1
        print("Attempts left: " + str(attempts))
if '_' not in word_display:
    print("You guessed the word!")
    print(" ".join(word_display))
    print("You survived")
else:
    print("You lost!. The word was: " + chosen_word)





