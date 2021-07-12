f1 = open('1a.txt', 'r')
data= ''.join(f1.readlines())
f2 = open('2a.txt','r')
toFind = f2.readline()
if data.find(toFind) != -1:
    print("ip "+toFind+" found!")
else:
    print("ip "+toFind+" not found!")
