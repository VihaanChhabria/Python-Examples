Choice = 0
Calc = 0

while int(Choice) != 5:
    Choice = input("Enter 1 for add, 2 for subtract, 3 for multiply, 4 for divide, 5 for Exit ")

    if int(Choice) == 5:
        exit()

    Num1 = input("Enter First Number ")
    Num2 = input("Enter Second Number ")

    if int(Choice) == 1:
        print("Add")
        Calc = float(Num1) + float(Num2)

    elif int(Choice) == 2:
        print("Subtact")
        Calc = float(Num1) - float(Num2)

    elif int(Choice) == 3:
        print("Multiply")
        Calc = float(Num1) * float(Num2)

    elif int(Choice) == 4:
        print("Divide")
        Calc = float(Num1) / float(Num2)

    else:
        print("INVALID CHOICE")

    print("Your Number is", Calc)