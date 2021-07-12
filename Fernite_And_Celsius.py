#Coverts Fernite and Celsius
print("f To Find Fernite")
print("c To Find Celsius")
Hi = input("")

if Hi == "c":
    Celsius = input("Celsius is ")

    Fernite = int(Celsius) / 5 * 9 + 32
    print(Fernite)

if Hi == "f":
    Fernite = input("Fernite is ")

    Celsius = int(Fernite) - 32 * 5 / 9
    print(Celsius)