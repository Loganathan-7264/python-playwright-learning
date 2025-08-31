num=int(input("Enter the number: "))
total = 0
while num>0:
    digit = num % 10 #taking the last digit
    total +=digit
    num=num//10 #removing the last digit

print(total)
