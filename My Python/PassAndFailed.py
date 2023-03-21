eng = int(input("Enter Marks of English:"))
nep = int(input("Enter Marks of Nepali:"))
sci = int(input("Enter Marks of Science:"))
maths = int(input("Enter Marks of Maths:"))
if (0<=eng<=100) and (0<=nep<=100) and (0<=sci<=100) and (0<=maths<=100) :
    if(eng>=40 and nep >=40 and sci >= 40 and maths >= 40):
        per=(eng+nep+sci+maths)/4
        if (per >= 40 and per <60) :
            print("You are passed in ThirdSecond Div.")
        elif (per >=60 and per <80) :
            print("You are god Fst Div.")
        elif (per >=80 and per <100) :
            print("You are got Dist.")    
    else:
        print("Your Filed")
else :
    print("Invalid MArks")
