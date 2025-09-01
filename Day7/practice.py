# mylist1 = ["a","b","c"]
# print(mylist1)
# mylist2=[10,20,30,40]
# print(mylist2)
# mylist3=["apple",10,"orange",20.00,"loga"]
# print(mylist3)
from Day6.mutableVSimmutable import mylist

# mylist1=["apple",10,"orange",20.00,"loga"]
# print(mylist1[-2])

# mylist1=["apple",10,"orange",20.00,"loga"]
# # print(mylist1[-4:-2])
#
# mylist1[1]="Tony"
# print(mylist1)

# mylist=["apple",10,"orange",20.00,"loga"]
# for i in mylist:
#     print(i)

# mylist=["apple",10,"orange",20.00,"loga"]
# if "apple" in mylist:
#     print("found")
# else:
#     print("not found")
# mylist=["apple",10,"orange",20.00,"loga", 10, 10, "apple"]
# print(len(mylist))
# print(mylist.count("apple"))
# mylist = ["cherry", "mango", "banana","kiwi", "apple"]
# mylist=[7,3,5,1,3,9,2]
# mylist.sort()
# # mylist.sort(reverse=True)
# print(mylist)
# mylist=[7,3,5,1,3,9,2]
# mylist.append("loga")
# mylist = ["cherry", "mango", "banana","kiwi", "apple"]
# mylist.insert(3,8)
# print(mylist)

# mylist = ["cherry", "mango", "banana", "kiwi", "apple"]
# mylist.remove("mango")
# mylist.pop(4)
# del mylist[0]
# mylist.clear()
# print(mylist)

mylist1=["Tony", "Stark"]
# mylist2=mylist1.copy()
mylist2=["Loga", "Nathan"]
# mylist1.extend(mylist2)
mylist3=list()
for i in mylist1:
    mylist3.append(i)
print(mylist3)