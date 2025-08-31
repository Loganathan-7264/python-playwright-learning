num=int(input("Enter the number: "))
reverse = 0
while num>0:
    digit = num % 10 #taking the last digit
    reverse = reverse * 10 + digit
    num = num //10

print(reverse)
