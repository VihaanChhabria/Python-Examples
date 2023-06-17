import random

def __create_keyboard_init():

    global letters
    letters = list("abcdefghijklmnopqrstuvwxyz")

    global chromo
    chromo = [[], [], []]
    global chromo_sections_lim
    chromo_sections_lim = [10, 9, 7]

def return_random_keyboard():

    __create_keyboard_init()

    for chromo_section_index, chromo_section in enumerate(chromo_sections_lim):
        for gene in range(chromo_section):
            random_letter = random.choice(letters)
            chromo[chromo_section_index].append([random_letter, max(0, chromo_section_index-0.5) + gene + 0.5])
            letters.remove(random_letter)

    #print(chromo)
    return chromo

#create_keyboard_init()
#print(return_random_keyboard())
#[[['w', 0], ['h', 1], ['f', 2], ['a', 3], ['c', 4], ['x', 5], ['t', 6], ['k', 7], ['z', 8], ['e', 9]],
#  [['o', 0.5], ['r', 1.5], ['n', 2.5], ['u', 3.5], ['y', 4.5], ['b', 5.5], ['s', 6.5], ['g', 7.5], ['m', 8.5]],
#  [['i', 1.5], ['l', 2.5], ['q', 3.5], ['p', 4.5], ['j', 5.5], ['v', 6.5], ['d', 7.5]]]