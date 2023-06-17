import CreateKeyboard
import GetDataSet
import FindDistance
import CombineKeyboards

FindDistance.find_distance_init()

initial_chromo = 3

total_chromo = []
for chromo_num in range(initial_chromo):
    total_chromo.append(CreateKeyboard.return_random_keyboard())



chromo_distances = []
for chromo_num in range(initial_chromo):
    chromo_distances.append([])

for i in range(5):
    dataset = list(GetDataSet.return_dataset())

    full_distance = 0

    for chromo_num, chromo in enumerate(total_chromo):
        for letter_index, letter in enumerate(dataset):
            if not (len(dataset) == letter_index+1):
                full_distance = full_distance + FindDistance.return_distance(chromo=chromo, start_letter=letter, end_letter=dataset[letter_index+1])

        chromo_distances[chromo_num].append(full_distance)
        full_distance = 0

for chromo_distance_index, chromo_distance in enumerate(chromo_distances):
    for single_try in chromo_distance:
        total = total + single_try

    chromo_distances[chromo_distance_index] = total/len(chromo_distance)
    total = 0

print(chromo_distances)