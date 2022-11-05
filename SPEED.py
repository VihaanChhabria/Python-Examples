while True:
    distance = 0
    time = 0
    speed = 0
    
    print("d To Find Distance")
    print("t To Find Time")
    print("s To Find Speed")
    choice = input("")

    if choice == "s":
        distance = input("Distance is ")
        time = input("Time is ")

        speed = int(distance) / int(time)
        print(speed)

    if choice == "t":
        distance = input("Distance is ")
        time = input("Speed is ")

        time = int(distance) / int(speed)
        print(time)

    if choice == "s":
        distance = input("Time is ")
        time = input("Speed is ")

        distance = int(time) * int(speed)
        print(speed)