
#Makes the area of a sqaure
Choice = input ("Enter 1 for area, 2 for permiter and 3 for exit ")
while int (Choice) !=3:
    if int(Choice) == 1:
        print("AREA")
        width = input ("What is width? ")
        lenght = input ("What is lenght? ")
        AREA = float(width)*float(lenght)
        print (float(AREA))

    elif int(Choice) == 2:
        print("perimiter")
        side1 = input ("What is side 1? ")
        side2 = input ("What is side 2? ")
        side3 = input ("What is side 3? ")
        side4 = input ("What is side 4? ")
        perimiter=float(side1) + float(side2) + float(side3) + float(side4)
        print (float(perimiter))
        
    Choice = input ("Enter 1 for area, 2 for permiter and 3 for exit ")