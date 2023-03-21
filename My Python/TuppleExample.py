mytupple= ("mango", "tomotto", 100, 10.6, 4+4j, 4+4j)
print(mytupple)
print(mytupple[0])
print(mytupple[2:4])
x = len(mytupple)
print(x)
mylist=list(mytupple)
print(mylist)
mylist[0]="Apple"
mytupple=tuple(mylist)
print(mytupple)
for i in mytupple:
    print(i)
i=0
while i < len(mytupple):
    print(mytupple[i])
    i=i+1
mytupple1=mytupple *4
print(mytupple1)
x = mytupple.index(4+4j)
print(x)
y=mytupple.count(4+4j)
print(y)
