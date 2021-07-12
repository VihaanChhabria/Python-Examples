#Calculatar
Choice=0
Choice=input("Enter 1 for add, 2 for subtract 3 for Multiply and 4 for Divide and 5 to Exit ")
while int(Choice) != 5:
    if int(Choice) == 1:
        print("Add")
        Num1=input("Enter First Number ")
        Num2=input("Enter Second Number ")
        #add 2 numbers
        sum=float(Num1)+float(Num2)
        print(float(sum))


    elif int(Choice) == 2:
        print("Subtract")
        Num1=input("Enter First Number ")
        Num2=input("Enter Second Number ")
        #subtract 2 numbers
        sub=float(Num1)-float(Num2)
        print(float(sub))


    elif int(Choice) == 3:
        print("Multiply")
        Num1=input("Enter First Number ")
        Num2=input("Enter Second Number ")
        #multiply 2 numbers
        mult=float(Num1)*float(Num2)
        print(float(mult))


    elif int(Choice) == 4:
        print("Divide")
        Num1=input("Enter First Number ")
        Num2=input("Enter Second Number ")
        #divide 2 numbers
        div=float(Num1)/float(Num2)
        print(float(div))


    else:
        print("INVALID CHOICE")

    Choice=input("Enter 1 for add, 2 for subtract 3 for Multiply and 4 for Divide and 5 to Exit")
