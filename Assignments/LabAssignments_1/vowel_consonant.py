#method 1

# letter = input("Enter a single letter: ").lower()
#
# if letter == "a":
#     print("Vowel")
# elif letter == "e":
#     print("Vowel")
# elif letter == "i":
#     print("Vowel")
# elif letter == "o":
#     print("Vowel")
# elif letter == "u":
#     print("Vowel")
# else:
#     print("Consonant")

# method 2

letter = input("Enter a single letter: ").lower()

if letter in "aeiou":
    print("Vowel")
else:
    print("Consonant")