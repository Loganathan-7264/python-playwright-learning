# #Arithmetic operators
# #   +  -  *  / //  %  **
#
# a= 11
# b=3
#
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)
# print(a**b)


#Relational Operators
#  >  <   >=    <=  ==   !=
# Relational operators always returns boolean value True/False

# a= 9
# b=10
# #
# print(a>b)   # False
# print(a<b)   #True
# print(a==b)  #False
# print(a!=b) #True

# b=9
# print(a==b)    #True
# print(a!=b)   #False
#
# print(a<=b)   #True
# print(a>=b)   #True


#Logical operators
#  and   or   not
# always returns boolean value True/False


#a      b       a and b     a or b      not a   not b
# ----------------------------------------------------
# T     T       T           T
# T     F       F           T
# F     T       F           T
# F     F       F           F


# Example 1
# a=True
# b=False
#
# print(a and b)  #False
# print(a or b)   #True
#
# print(not a)  #False
# print(not b)  #True
#


# combination of both relational and logical operators
print((1>2))  # F
print((1<2))  # T

print( (1<2) and (1>2))   #False
print( (1<2) or (1>2))   #  True
