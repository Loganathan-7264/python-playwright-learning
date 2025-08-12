Day 2 – Python Basics
Topics Covered
Deleting Variables

Data Types

Operators

Concatenation

User Input

Type Conversion / Type Casting

1. Deleting Variables
Use del to remove a variable from memory.

Once deleted, you cannot use it until recreated.

python
Copy
Edit
a = 100
b = 200
del a
print(b)  # Works → 200
2. Basic Data Types
int → Whole numbers (10, -5)

float → Decimal numbers (3.14, -0.5)

str → Text/strings ("Hello", 'Python')

bool → True or False

python
Copy
Edit
x = 100       # int
y = 10.5      # float
s = "Python"  # str
b = True      # bool
print(type(x))  # <class 'int'>
3. Operators
Arithmetic: +, -, *, /, %, ** (power), // (floor division)

Comparison: ==, !=, >, <, >=, <= → returns True/False

Logical: and, or, not

4. Concatenation
+ joins same-type values.

Works for strings, numbers, and booleans (True = 1, False = 0).

python
Copy
Edit
print('Hello' + 'Python')  # HelloPython
print(True + 5)            # 6
5. Taking User Input
input() always returns a string.

Convert to number if needed.

python
Copy
Edit
name = input("Enter name: ")
num1 = int(input("Enter number: "))
num2 = float(input("Enter decimal: "))
6. Type Casting
Change data type: int(), float(), str().

python
Copy
Edit
x = "10"
y = int(x)  # "10" → 10