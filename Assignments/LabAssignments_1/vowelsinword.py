word=input("Enter the word: ").lower()
vowel="aeiou"
count =0

for char in word:
    if char in vowel:
        count+=1
print(count)