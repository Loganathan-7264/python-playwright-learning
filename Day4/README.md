Day 4 – Match, Range & Loops in Python
🔹 Match Statement

Works like a switch in other languages.

Helps avoid long if...elif...else chains.

Syntax:

match expression:
    case value1:
        # code
    case value2:
        # code
    case _:
        # default (if nothing matches)


How it works:

Expression is checked once.

Compared with each case.

Runs the matching block.

🔹 range() Function

Used to generate a sequence of numbers.

Syntax: range(start, stop, step)

start → default 0

stop → exclusive (not included)

step → default 1 (can be negative too)

🔹 Looping Statements

While Loop – Runs as long as condition is True.

while condition:
    # code


For Loop – Runs a fixed number of times (mostly with range()).

for i in range(start, stop, step):
    # code

🔹 Jumping Statements

break → exits the loop immediately.

continue → skips the current iteration, moves to next.