#This is a simple program which lets a user check if a word is palindrome or not.

word = input("Enter a word:")
word = word.upper()
rev_word = word[::-1]

if word == rev_word:
    print("The word you entered is palindrome!")
else:
    print("The word you entered is not palindrome!")

input("Press any button to exit...")