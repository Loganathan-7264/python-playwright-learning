📝 Day 5 & 6– Python Strings
🔹 Creating Strings

" " → double quotes

' ' → single quotes

str() → constructor

name = "John"
grade = 'B'
empty = str()      # empty string
print(type(name))  # <class 'str'>


⚡ Strings are always objects of str.

🔹 String Operators

+ → join strings

* → repeat string

s = "welcome"
print(s + " python")   # welcome python
print(s * 3)           # welcomewelcomewelcome

🔹 Slicing Strings

Index starts from 0 (left → right)

Negative index → (right → left)

mystr = "welcome"
print(mystr[1:3])   # el
print(mystr[:6])    # welcom
print(mystr[2:])    # lcome
print(mystr[1:-1])  # elcom
print(mystr[-5:-2]) # lco


👉 s[::-1] → reverse string

🔹 f-Strings (Formatting)
age = 30
print(f"My name is John, I am {age}")  

price = 59
print(f"The price is {price:.2f} dollars")  # 59.00


⚡ Old way: "Hello {}".format(name)

🔹 Membership Operators
s = "welcome"
print("come" in s)      # True
print("lome" not in s)  # True

🔹 Strings are Immutable

❌ You can’t change them directly.
✅ You must create a new one.

s1 = "hello"
# s1[0] = "H"  # ❌ error
s2 = "H" + s1[1:]   # ✅

🔹 String Methods

👉 Case Conversion

"hello".capitalize()  # Hello
"Hello".lower()       # hello
"Hello".upper()       # HELLO
"welcome to python".title()  # Welcome To Python
"Hello".swapcase()    # hELLO


👉 Search & Replace

s = "banana"
print(s.count("a"))       # 3
print(s.replace("ana", "xy"))  # bxyna


👉 Validation (Checks)

"abc123".isalnum()   # True
"hello".isalpha()    # True
"123".isdecimal()    # True
"²".isdigit()        # True (superscript 2)
"⅔".isnumeric()      # True (fraction 2/3)


👉 Split & Join

s = "one,two,three"
print(s.split(","))   # ['one','two','three']


👉 Start/End Check

"hello".startswith("he")  # True
"file.py".endswith(".py") # True


👉 Trim Spaces

" hello ".strip()   # hello
" hello".lstrip()   # hello
"hello ".rstrip()   # hello

🔹 Summary

Strings = Immutable (cannot modify in place).

Main uses: slicing, formatting, searching, validation.

Key methods:

Case: lower(), upper(), title(), capitalize()

Find/Count: find(), index(), count(), replace()

Validation: isalpha(), isdigit(), isnumeric()

Utility: split(), strip(), startswith(), endswith()