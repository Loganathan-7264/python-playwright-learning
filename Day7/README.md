📝 Day 7 Notes: Python Collections – List
✅ What is a List?

Ordered → items have positions (index).

Mutable → can change (add, update, remove).

Duplicates allowed.

Written inside [ ].

🎯 Creating Lists
mylist1 = [10, 20, 30, 40, 50]
mylist2 = ["apple", "banana", "cherry"]
mylist3 = ["apple", 10, "banana", 20]   # mixed
mylist4 = list()  # empty list

🎯 Accessing Items
mylist = ["apple", "banana", "cherry"]

print(mylist[0])   # apple
print(mylist[-1])  # cherry  (negative index → from end)

🎯 Slicing
mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(mylist[2:5])    # ['cherry', 'orange', 'kiwi']
print(mylist[-4:-1])  # ['orange', 'kiwi', 'melon']

🎯 Change Item
mylist = ["apple", "banana", "cherry"]
mylist[1] = "orange"
print(mylist)  # ['apple', 'orange', 'cherry']

🎯 Looping
for item in mylist:
    print(item)

🎯 Check if Exists
if "apple" in mylist:
    print("Yes, apple is present")

🎯 List Functions
print(len(mylist))        # length
print(mylist.count("apple"))  # count occurrences

🎯 Sorting & Reversing
mylist = ["cherry", "mango", "banana", "apple"]

mylist.sort()
print(mylist)  # ['apple', 'banana', 'cherry', 'mango']

mylist.sort(reverse=True)
print(mylist)  # ['mango', 'cherry', 'banana', 'apple']

mylist.reverse()
print(mylist)  # ['apple', 'banana', 'cherry', 'mango']


⚠️ Heterogeneous data (mix of str + int) → TypeError in sort.

🎯 Adding Items
mylist = ["apple", "banana"]
mylist.append("cherry")      # add at end
mylist.insert(1, "orange")   # insert at index

🎯 Removing Items
mylist.remove("banana")  # by value
mylist.pop(0)            # by index
del mylist[1]            # delete specific
mylist.clear()           # remove all

🎯 Copying a List
mylist1 = ["apple", "banana"]
mylist2 = mylist1.copy()

🎯 Joining Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

print(list1 + list2)  # using +
list1.extend(list2)   # using extend()


🔥 Key Point:
Lists are mutable → you can update them anytime.