#Reads to diles then compares them
a_file = open("1a.txt")
b_file = open("2a.txt")

linesA = a_file.readlines()
linesB = b_file.readlines()

print(linesA)
print(linesB ,"\n")

if linesA == linesB:
    print("equal")

else:
    print("not equal")