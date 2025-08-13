Day 3 – Python Conditional Statements
What they do?
Used to make decisions in code.

Runs different code blocks based on True / False conditions.

Indentation
Python uses spaces/tabs to define code blocks (no {} like Java/C++).

Wrong indentation = error.

1. if Statement
✅ Runs code only if condition is True.

python
Copy
Edit
age = 18
if age >= 18:
    print("You are eligible to vote.")
# Output: You are eligible to vote.
2. if...else
✅ if runs if condition is True, else runs if condition is False.

python
Copy
Edit
age = 16
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
# Output: You are not eligible to vote.
3. if...elif...else
✅ Multiple conditions.

python
Copy
Edit
marks = 75
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Fail")
# Output: Grade: B
4. Short Hand If
✅ One-line if

python
Copy
Edit
if a > b: print("a is greater than b")
5. Short Hand If...Else (Ternary)
✅ One line for if and else.

python
Copy
Edit
a = 2; b = 330
print("A") if a > b else print("B")
✅ Multiple conditions in one line:

python
Copy
Edit
a = 330; b = 330
print("A") if a > b else print("=") if a == b else print("B")
6. Logical Operators in Conditions
and → Both must be True

python
Copy
Edit
if a > b and c > a:
    print("Both conditions are True")
or → At least one True

python
Copy
Edit
if a > b or a > c:
    print("At least one condition is True")
not → Reverse the result

python
Copy
Edit
if not a > b:
    print("a is NOT greater than b")
7. Nested if
✅ if inside if

python
Copy
Edit
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
8. pass Statement
✅ Placeholder when code is empty.

python
Copy
Edit
if b > a:
    pass  # no action for now
💡 Quick Recap
if → one condition
if...else → two paths
if...elif...else → multiple paths
and / or / not → combine conditions
pass → skip for now

