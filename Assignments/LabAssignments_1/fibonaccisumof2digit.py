n=int(input("Enter the number: "))

a,b=0,1
print(a,b)
for i in range(2,n):
    c=a+b
    print(c)
    a=b
    b=c