import math

def find_distance_init():

    global cache
    cache = []

def __find_coord(chromo, letter):

    for letter_set in cache:
        if letter in letter_set:
            return letter_set[1]
            

    for row_num, row in enumerate(chromo):
        for gene in row:
            #print(gene)
            #print(start_letter)
            #time.sleep(0.1)
            if letter in gene:
                print("in")
                coord = [gene[1], row_num]
                return coord

def return_distance(chromo, start_letter, end_letter):

    start_letter_coords = []
    
    end_letter_coords = []

    start_letter_coords = __find_coord(chromo, start_letter)

    end_letter_coords = __find_coord(chromo, end_letter)
                
    print(start_letter_coords)
    print(end_letter_coords)
    distance = math.sqrt(pow(end_letter_coords[0] - start_letter_coords[0], 2) + pow(end_letter_coords[1] - start_letter_coords[1], 2))

    return distance
