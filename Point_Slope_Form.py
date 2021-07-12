#Finds point slope form
x = "x"
x1 = input("")
y1 = input("")
x2 = input("")
y2 = input("")

m = (int(y2) - int(y1)) / (int(x2) - int(x1))


exp1 = str(m) + x
exp2 = int(y1) - m*int(x1)


print(exp1)

print(str(exp2))

sign = "+"

if (exp2 < 0):
    sign = ""

y = exp1 + sign + str(exp2)
print("y =", y)
