#6/15/2021
#Does diffrent things with a list

NUMBERS_LIST = []
holder = 0
sum = 0
a = 0

def rotate():
    a = NUMBERS_LIST[0]
    NUMBERS_LIST.append(a)
    NUMBERS_LIST.pop(0)
    print("Rotated!", NUMBERS_LIST)

Number_Amount = input("How many numbers do you want to put into the system? ")

while holder < int(Number_Amount):
    Numbers_Ask = input("Whats your number? ")
    Numbers_Ask = int(Numbers_Ask)
    NUMBERS_LIST.append(Numbers_Ask)
    holder = holder + 1

NUMBERS_LIST.sort()
print("Your list in ascending order: ", NUMBERS_LIST)

NUMBERS_LIST.sort(reverse = True)
print("Your list in descending order: ", NUMBERS_LIST)

print("You have ", len(NUMBERS_LIST), " element(s)")

counter = 0
while counter < len(NUMBERS_LIST):
    sum = sum + NUMBERS_LIST[counter]
    counter = counter + 1
print("The sum of all your numbers is ", sum)

rotate()
rotate()
rotate()
rotate()
rotate()
rotate()
rotate()
rotate()
rotate()
rotate()