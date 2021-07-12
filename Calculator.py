#Calcutater
Choice=0
Calc=0
Choice=input("Enter 1 for add, 2 for subtract 3 for Multiply and 4 for Divide and 5 to Exit ")
while int(Choice) != 5:
    Num1=input("Enter First Number ")
    Num2=input("Enter Second Number ")

    if int(Choice) == 1:
        print("Add")
        #add 2 numbers
        Calc=float(Num1)+float(Num2)


    elif int(Choice) == 2:
        print("Subtract")
        #subtract 2 numbers
        Calc=float(Num1)-float(Num2)


    elif int(Choice) == 3:
        print("Multiply")
        #multiply 2 numbers
        Calc=float(Num1)*float(Num2)


    elif int(Choice) == 4:
        print("Divide")
        #divide 2 numbers
        Calc=float(Num1)/float(Num2)


    else:
        print("INVALID CHOICE")

    print(float(Calc))
    Choice=input("Enter 1 for add, 2 for subtract 3 for Multiply and 4 for Divide and 5 to Exit")