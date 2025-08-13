# # name="John"
# # age=30
# # sal=50000.50
#
# name,age,sal="john",30,50000.50
# # print(name, age, sal)
#
# # print("Name is:"+name) # valid
# # print("Age is:"+age) #not valid
# # print(("Name is:", name))
# # print("age is:", age)
# # print("Name is %d, age is %s, sal is %g" %(age,name,sal))
# # print("Name is {}, age is {}, sal is {}".format(sal, age,name))
# # print("Name is {1}, age is {1}, sal is {2}".format(name,age,sal))
from sys import flags
from time import process_time_ns

#  E-commerce Discount Calculator
# amount = int(input("Enter the product amount: ")) #getting input from the user
#
# if amount >= 1000:
#     discount = amount * 20/100
#     print("Your final amount after applying the discount: ", amount-discount)
# elif amount >=500:
#     discount = amount * 10/100
#     print("Your final amount after applying the discount:", amount-discount)
# else:
#     print("Discount not applied, Final amount: ", amount)

# Banking — Simple Interest Calculator

# principle = int(input("Enter your principle amount: "))
# Intrest_rate = int(input("Enter your intrest rate: "))
# Time = int(input("Enter the term period (in years): "))
# SI = (principle*Intrest_rate*Time)/100
# print("Your intrest amount is: ", SI)

# # Movie Ticket Booking System
# age = int(input("Enter your age: "))
# if age < 12:
#     print("Ticket price is 100")
# elif 12 <= age <= 60:
#     print("Ticket price is 150")
# elif age>60:
#     print("Ticket price is 120")

# Fitness App — BMI Calculator
weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))
BMI = weight/(height*height)
if BMI <18.5:
    print("Underwight!!")
elif BMI >=18.5 and BMI <24.9:
    print("Normal")
elif BMI >= 25 and BMI <= 29.9:
    print("Overweight")
else:
    print("Obese!!!")