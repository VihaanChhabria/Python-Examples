#Finds speed
while True :
    print("d To Find Distance")
    print("t To Find Time")
    print("s To Find Speed")
    Hi = input("")

    if Hi == "s":
        Distance = input("Distance is ")
        Time = input("Time is ")

        Speed = int(Distance) / int(Time)
        print(Speed)

    if Hi == "t":
        Distance = input("Distance is ")
        Speed = input("Speed is ")

        Time = int(Distance) / int(Speed)
        print(Time)

    if Hi == "d":
        Time = input("Time is ")
        Speed = input("Speed is ")

        Distance = int(Time) * int(Speed)
        print(Distance)