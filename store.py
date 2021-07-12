#A Store
mangoTotal = 0
bannanaTotal = 0
appleTotal = 0
orangeTotal = 0    
NoYes = True
NoYesAns = 0
FRUITtotal = 0
choice = 0

while NoYes:

    print ("1 - MANGO costs $1.50")
    print ("2 - BANNANA costs $0.50")
    print ("3 - APPLE cost $1.00")
    print ("4 - ORANGE cost $0.75")

    choice = input ("Do you want any of these items. 1 for yes, 2 for no. ")

    if int (choice) == 2:
        NoYes = False
        print("The total cost for fruit is  $", FRUITtotal)
        exit()

    fruit = input("Please Type 1 for mango, 2 for banana, 3 for apple, 4 for orange ")
    if  (int(fruit) >= 1) and (int(fruit) <=4):


        if int(fruit) == 1:
            mangoNum = input("How many? ")
            mangoTotal = mangoTotal + 1.50 * int(mangoNum)
            

        elif int(fruit) == 2:
            bannanaNum = input("How many? ")
            bannanaTotal = bannanaTotal + 0.50 * int(bannanaNum)

        elif int(fruit) == 3:
            appleNum = input("How many? ")
            appleTotal = appleTotal + 1.00 * int(appleNum)
            

        elif int(fruit) == 4:
            orangeNum = input("How many? ")
            orangeTotal = orangeTotal + 0.75 * int(orangeNum)
        
        FRUITtotal = FRUITtotal + orangeTotal + appleTotal + bannanaTotal + mangoTotal

    NoYesAns = input("Do you want to continue. Type 1 for yes, and 2 for no. ")
    if NoYesAns == 2:
        NoYes = False
        print("The total cost for fruit is  $", FRUITtotal)
        exit()

    else:
        orangeTotal = 0
        appleTotal = 0
        bannanaTotal = 0
        mangoTotal = 0