import random
import CreateKeyboard

def __return_half_list(chromo):
    halfLimits = [5, 4, 4]

    leftHalf = []
    rightHalf = []

    for row_index, row in enumerate(chromo):
        leftHalfRow, rightHalfRow = __return_half_row(row, halfLimits[row_index])
        leftHalf.append(leftHalfRow)
        rightHalf.append(rightHalfRow)

    return leftHalf, __return_clean_list(rightHalf, True)

def __return_half_row(row, limit):

    leftHalfRow = []
    rightHalfRow = row

    for letter_index, letter in enumerate(row):
        if not (letter_index == limit):
            leftHalfRow.append(letter[0])
            rightHalfRow.remove(letter)

    return leftHalfRow, rightHalfRow

def __return_clean_list(nested_list, nested):

    if not nested:
        clean_list = []
    else:
        clean_list = [[], [], []]

    for row_index, row in enumerate(nested_list):
        for letter in row:
            if not nested:
                clean_list.append(letter[0])
            else:
                clean_list[row_index].append(letter[0])

    return clean_list

def __return_splits(chromoList):

    left_splits = []
    right_splits = []
    for chromo in chromoList:
        halfLists = __return_half_list(chromo)
        left_splits.append(halfLists[0])
        right_splits.append(halfLists[1])
    return left_splits, right_splits

def return_mixed_keyboard(chromoList, chromoReturns):

    finalChromoLists = []

    left_splits, right_splits = __return_splits(chromoList)

    for i in range(chromoReturns):
        chromoL1 = random.choice(left_splits)
        chromoR2 = random.choice(right_splits)

        flat_chromoL1 = __return_clean_list(chromoL1, False)
        flat_chromoR2 = __return_clean_list(chromoR2, False)

        alpha = list("abcdefghijklmnopqrstuvwxyz")

        repeated = []


        for row_index, row in enumerate(chromoR2):
            for letter_index, letter in enumerate(row):
                if letter in flat_chromoL1:
                    repeated.append([row_index, letter_index])
                    chromoR2[row_index][letter_index] = None



        filtered = (list(filter(lambda x: x not in flat_chromoL1+flat_chromoR2, alpha)))
        random.shuffle(filtered)
        if not (filtered == []):
            for empty_placement_index, empty_placement in enumerate(repeated):
                chromoR2[empty_placement[0]][empty_placement[1]] = filtered[empty_placement_index]

        reconstructed = chromoL1
        for chromoR2_row_index, chromoR2_row in enumerate(chromoR2):
            reconstructed[chromoR2_row_index] = reconstructed[chromoR2_row_index] + chromoR2_row
        finalChromoLists.append(reconstructed)

    return finalChromoLists

#print(return_mixed_keyboard([CreateKeyboard.return_random_keyboard(), CreateKeyboard.return_random_keyboard(), CreateKeyboard.return_random_keyboard(), CreateKeyboard.return_random_keyboard()], 3))
