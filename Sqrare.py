choice = 0
while True:
    choice = input("Enter 1 for area, 2 for permiter and 3 for exit ")

    if int(choice) == 1:
        print("Area")
        width = input("What is you width? ")
        lenght = input("What is you lenght? ")
        area = float(lenght) * float(width)
        print(area)

    elif int(choice) == 2:
        print("Permeter")
        side1 = input("Whats the lenght of side 1?")
        side2 = input("Whats the lenght of side 2?")
        side3 = input("Whats the lenght of side 3?")
        side4 = input("Whats the lenght of side 4?")
        permeter = float(side1) + float(side2) + float(side3) + float(side4)
        print(permeter)

    elif int(choice) == 3:
        exit()
