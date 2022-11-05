factor_number = 1
counter = True
NegOrPos = True

print("ax^2 + bx + c")

a = float(input("Value for a: "))
b = float(input("Value for b: "))
c = float(input("Value for c: "))
c = c*a

def gcd(a, b):
    
    a, b = b, a%b
    return a

while counter:
    if factor_number == 0:
        factor_number = -1
    factor = c/factor_number
    if factor + factor_number == b:
        factor_S = factor/a
        factor_number_S = factor_number/a
        if factor_number_S - int(factor_number_S) == 0 and factor_S - int(factor_S) == 0:
            factor_S_P = "(x + " + str(int(factor_S)) + ")"
            factor_number_S_P = "(x + " + str(int(factor_number_S)) + ")"
            counter = False
        else:
            factor_S = gcd(factor, a)
            factor_number_S = gcd(factor_number, a)

            factor_S_P = "(" + str(int(gcd(factor, a))) + "x + " + str(int(factor/gcd(factor, a))) + ")"
            factor_number_S_P = "(" + str(int(gcd(factor_number, a))) + "x + " + str(int(factor_number/gcd(factor_number, a))) + ")"
            counter = False

    if factor_number > c:
        NegOrPos = False
    if NegOrPos:
        factor_number = factor_number + 1
    else:
        factor_number = factor_number - 1

print(factor_S_P)
print(factor_number_S_P)