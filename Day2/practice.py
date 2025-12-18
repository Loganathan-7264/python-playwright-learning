# # swapping
# a = int(input("Enter number a: "))
# b = int(input("Enter number for b:"))
# c = int(input("Enter number for c:"))
#
# # before swapping
# print(a,b,c)
# # swapping
# a,b,c = b,c,a
# # after swapping
# print(a,b,c)

# # weired calculator
# x=int(input("enter a number for x:"))
# y=int(input("enter a number for y:"))
# z=str(x+y)
# print(z)
# print(z*3)

# #Boolea Trickery
# value1=bool(input("enter True: "))
# value2=bool(input("enter False: "))
# print(value1 and value2)
# print(value1 or value2)
# print(not value1)
# print(not value2)

# # Boolean Trickery (fixed version)
# value1 = input("Enter True or False: ").strip().lower() == "true"
# value2 = input("Enter True or False: ").strip().lower() == "true"
#
# print(value1 and value2)
# print(value1 or value2)
# print(not value1)
# print(not value2)

# Final Price Calculator
# item_price = float(input("Enter the amount of item: " ))
# GST_percentage = float(input("Enter the GST percentage: "))
# Discount_percentage = float(input("Enter the Discount percentage: "))
#
# GST_amount = (item_price * GST_percentage)/100
# Discount_amount = (item_price * Discount_percentage)/100
#
# Final_Price = (item_price + GST_amount) - Discount_amount
# print(Final_Price)

item_price = float(input("Enter the amount of product: "))
gst_per = float(input("enter the gst %: "))
discount_per = float(input("Enter the discount %: "))

gst_amount = (item_price*gst_per)/100
discount_amount = (item_price*discount_per)/100
final_price = (item_price + gst_amount) - discount_amount
print(("Final price of product is: ", final_price))