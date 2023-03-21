marks=int(input("Enter Marks: "))
if marks>=0 and marks <=100 :
    if marks >=40 :
        if marks >=40 and marks <60 :
            print("You are passed in Second Division")
        if marks >=60 and marks <80:
            print("You are passed in First Division")
        if marks >=80 and marks <=100 :
            print("You are passed in Distinction ")
    else :
        print("Your are failed")
else :
    print("invalid marks")
