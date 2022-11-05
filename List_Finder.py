a = [[1,2],[3,4,5]]

def in_list(item,L):
    for i in L:
        if item in i:
            b = L.index(i)
            return b
    return -1

def in_list2(item,L):
    for i in L:
        if item in i:
            b = i.index(item)
            return b
    return -1

print(in_list(1,a))
print(in_list2(5,a))