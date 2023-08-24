def is_vowel(letter):
    vowels = "aeiouAEIOU"
    return letter in vowels


input_letter = input("Enter a letter: ")

if len(input_letter) == 1 and input_letter.isalpha():
    if is_vowel(input_letter):
        print(f"{input_letter} is a vowel.")
    else:
        print(f"{input_letter} is not a vowel.")
else:
    print("Please enter a valid single letter.")