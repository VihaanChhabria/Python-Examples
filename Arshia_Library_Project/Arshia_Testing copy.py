triangle = [["harry potter", "ignite me", "Vihaan is a Potato"], ["the libray of lost things", "american royals"], ["cinder", "stiff"]]


max_book_len = 24
counter = 0

def display_shelf(list_name):
    for shelf_row in list_name:
        row_books = ""
        for shelf_col in shelf_row:
            num_space_char = max_book_len - len(shelf_col) + 5
            space_char = ""
            counter = 0
            while counter <= num_space_char:
                space_char = space_char + " "
                counter = counter + 1
            row_books = row_books + shelf_col + space_char
        print(row_books)

print(display_shelf(triangle))

########################################################################################################