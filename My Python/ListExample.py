mylist=["mango", "Apple", "Grepe", "Apple"]
#mylist.reverse()
p = mylist.index("Grepe")
print(p)

print(mylist)
print(type(mylist))
mylist.sort(key=str.lower)
print(mylist)
z = mylist.copy()
print(z)
x = mylist.count("Apple")
print(x)
mylist1=["ram", "sita"]
mylist=mylist+mylist1
print(mylist)
#mylist.extend(mylist1)
print(mylist)
mylist.insert(2,"Hari")
print(mylist)
mylist.pop(2)
print(mylist)
mylist.remove("Grepe")
print(mylist)


"""append/cls/len/copy/count/reverse/remove/pop/insert/sort
for i in mylist:
    print(i)
#constructor through list initialization.
age = list((2,3,4,4,5,6,7,8,9,10))
print(age) 
print(len(age))
age.append("Ram")
print(age)
print(age[0:5])
print(age[-11])
age.clear()
print(age)
i = 1
while i < len(mylist):
    print(mylist[i])
    i= i+1

mylist.sort()
print(mylist)
age = list((2,3,7,8,4,4,5,6,9,10))
age.sort(reverse=True)
print(age)
"""