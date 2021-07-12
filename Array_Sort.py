#sorts inputed letters
names = []
run = input("how many letters ")
counter = 0
while counter < int(run):
    words = input("letters please ")
    names.append(words)
    counter = counter + 1

hi = sorted(names)
print(hi)
