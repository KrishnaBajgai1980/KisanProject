marks = int(input("Enter Marks: "))
if marks >=0 and marks <=100 :
    if marks >= 40 :
        if marks >= 40 and marks <60 :
            print("you are Second Division")
        elif marks >=60 and marks < 80 :
            print("you are got First Division")
        elif marks >= 80 and marks <100 :
            print("you are got Distinction ")    
    else :
        print("You are Failed")
else :
    print("Invalid Marks")
