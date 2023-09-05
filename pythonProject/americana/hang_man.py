def hangman():
    word = "sheyge"
    guessed_letters = []
    tries = 6

    while tries > 0:
        guessed_word = ""
        for letter in word:
            if letter in guessed_letters:
                guessed_word += letter
            else:
                guessed_word += "_"

        print("Current word:", guessed_word)
        print_hangman(tries)

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct!")
        else:
            print("Incorrect!")
            tries -= 1

        if "_" not in guessed_word:
            print("Congratulations, you guessed the word:", word)
            break

    if tries == 0:
        print("Sorry, you ran out of tries. The word was:", word)


def print_hangman(tries):
    hangman_diagram = [
        "   _______",
        "   |     |",
        "   |     " + ("O" if tries < 6 else ""),
        "   |    " + ("/" if tries < 4 else "") + ("|" if tries < 5 else "") + ("\\" if tries < 3 else ""),
        "   |    " + ("/" if tries < 2 else "") + " " + ("\\" if tries < 1 else ""),
        "___|___"
    ]

    for line in hangman_diagram:
        print(line)


hangman()