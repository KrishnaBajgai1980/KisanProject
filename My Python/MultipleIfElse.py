eng=int(input("Enter Marks Of Subject: English::"))
maths=int(input("Enter Marks Of Subject: Maths::"))
Science=int(input("Enter Marks Of Subject: Science::"))
Nepali=int(input("Enter Marks Of Subject: Nepali::"))
Social=int(input("Enter Marks Of Subject: Social::"))
Computer=int(input("Enter Marks Of Subject: Computer Science::"))
Optional=int(input("Enter Marks Of Subject: Optional Maths/Economic::"))
tot=int(eng+maths+Science+Nepali+Social+Computer+Optional)
per=float(tot/7)
if per >= 90 and per <= 100 :
    print("Percentage:: ",per)
    print("GRADE ::","A+")
elif per >= 80 and per < 90 :
    print("Percentage::",per)
    print("GRADE ::","A")
elif per >= 70 and per < 80 :
    print("Percentage::",per)
    print("GRADE ::","B+")
elif per >= 60 and per < 70 :
    print("Percentage::",per)
    print("GRADE ::","B")
elif per >= 50 and per < 60 :
    print("Percentage::",per)
    print("GRADE ::","C+")
elif per >= 40 and per < 50 :
    print("Percentage::",per)
    print("GRADE ::","C")
elif per >= 30 and per < 40 :
    print("Percentage::",per)
    print("GRADE ::","D+")
elif per >= 20 and per < 30 :
    print("Percentage::",per)
    print("GRADE ::","D")
else :
    print("Percentage::",per)
    print("GRADE ::","E+")

