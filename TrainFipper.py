import string

initialFlip = 'a'
finalFlip = 'x'
flippers = list(string.ascii_lowercase)
print(flippers)

countInitial = 0
countFinal = 0
countCurrent = 0

if initialFlip in flippers:
    countInitial = flippers.index(initialFlip)
    print(countInitial)

    countFinal = flippers.index(finalFlip)
    print(countFinal)

    while not(countCurrent == countFinal):
        print("5")