junctions = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (1, 2), (2, 2)]
selected = (-1, -1)
list_selected = []
list_selected_path = []
x = 0
y = 1
BIN_var = True
started = (2, 0)

def list_appender(x):
    list_selected.append(x)
    list_selected_path.append(x)

def starting_junction(junction):
    if junction not in junctions:
        print("please try again")
        return False
    else:
        return True
'''
def adjacent_junction_cycle(adjacent_junction, selected_2nd):
    if selected_2nd in adjacent_junction:
        return True
'''

def selector():
    selected = (float(input("X Position of Junction Selected: ")), float(input("Y Position of Junction Selected: ")))
    if starting_junction(selected) == False:
        selector()
    else:
        list_selected.append(selected)
        return
    print("done\n")

def connection_checker(started):

    if not (2, 0) in list_selected:
        return True
    else:
        adjacent_junction = [(started[x] - 1, started[y] - 1), (started[x], started[y] - 1), (started[x] + 1, started[y] - 1), (started[x] - 1, started[y]), (started[x] + 1, started[y]), (started[x] - 1, started[y] + 1), (started[x], started[y] + 1), (started[x] + 1, started[y] + 1)]
        adjacent_loop = 0
        while adjacent_loop < len(adjacent_junction):
            if adjacent_junction[adjacent_loop] in list_selected_path:
                list_selected_path.remove(started)
                started = adjacent_junction[adjacent_loop]
                connection_checker()
            adjacent_loop = adjacent_loop + 1
    if (started == (0, 1)) or (started == (1, 1)) or (started == (1, 2)) and (0, 2 in list_selected):
        print("doone")
        return False



####



BIN_var = True

while BIN_var:
    selector()
    BIN_var = connection_checker(started)
    


'''
BIN_var = True
while BIN_var:
    selected_2nd = (float(input("X Position of next Junction Selected: ")), float(input("Y Position of next Junction Selected: ")))
    if starting_junction(junctions, selected_2nd) == False:
        continue
    else:
        adjacent_junction = ((selected[x] - 1, selected[y] - 1), (selected[x], selected[y] - 1), (selected[x] + 1, selected[y] - 1), (selected[x] - 1, selected[y]), (selected[x] + 1, selected[y]), (selected[x] - 1, selected[y] + 1), (selected[x], selected[y] + 1), (selected[x] + 1, selected[y] + 1))
        if adjacent_junction_cycle(adjacent_junction, selected_2nd):
            BIN_var = False
        else:
            continue
print("doone")
'''
