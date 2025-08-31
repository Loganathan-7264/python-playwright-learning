word = input("Enter the word: ").lower()

count_a =0
count_b =0
for ch in word:
    if ch=="a":
        count_a+=1
    elif ch=="b":
        count_b+=1
    else:
        continue
print(count_a)
print(count_b)