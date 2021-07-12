#Prints out whats in a txt file
names = []

a_file = open("1a.txt")

lines = a_file.readlines()
for line in lines:
    names.append(line)

names.sort()
print(names)
    