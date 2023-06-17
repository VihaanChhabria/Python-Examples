import wikipedia
import re

def return_dataset():

    # Set the language for the Wikipedia articles
    wikipedia.set_lang('en')

    # Minimum length threshold for the article content
    minimum_length = 500

    while True:
        # Fetch a random article
        random_page = wikipedia.random(pages=1)

        # Fetch the content of the random article
        page_content = wikipedia.page(random_page).content

        # Remove lines starting with "==" and empty lines
        page_content = re.sub(r'^==.*\n|\n', '', page_content, flags=re.MULTILINE)

        # Remove non-alphabetic characters and convert to lowercase
        page_content = re.sub(r'[^a-z]', '', page_content.lower())

        # Check if the content meets the minimum length requirement
        if len(page_content) >= minimum_length:
            break

    return page_content

"""
CreateKeyboard.create_keyboard_init()
FindDistance.find_distance_init()

full_distance = 0


chromo = CreateKeyboard.return_random_keyboard()

dataset = list(return_dataset())
print(dataset)

for letter_index, letter in enumerate(dataset):
    if not (len(dataset) == letter_index+1):
        print(dataset[letter_index+1])
        full_distance = full_distance + FindDistance.return_distance(chromo=chromo, start_letter=letter, end_letter=dataset[letter_index+1])

print(full_distance)"""