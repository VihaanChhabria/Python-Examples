import humanize

triangle = [["harry potter", "ignite me"], ["the libray of lost things", "american royals"], ["cinder", "stiff"]]
circle = [["eleven", "give and take"], ["amoung us", "black out"], ["one last stop", "fire with fire"]]
square = [["chosen", "tweet cute"], ["infinity son", "if we were us"], ["midnight sun", "camp"]]
star = [["boys dont knit", "smile"], ["drama", "idetical"], ["crank", "pawn"]]
heart = [["crossover", "everything everthing"], ["refuge", "red queen"], ["the book theif", "if i stay"]]
moon = [["heros", "tenderness"], ["girl in peices ", "wonder"], ["sheets", "they both die in the end"]]

bin_triangle = True
bin_circle = True
bin_square = True
bin_star = True
bin_heart = True
bin_moon = True

path = "Book Not Found"
max_book_len = 24

def find_book(book, list_name):
    for shelf_row in list_name:
        if book in shelf_row:
            inner = shelf_row.index(book)
            outer = list_name.index(shelf_row)
            return inner, outer
    return -1

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
print("Triangle")
print("--------")
print(display_shelf(triangle))
print()
print("Circle")
print("------")
print(display_shelf(circle))
print()
print("Square")
print("------")
print(display_shelf(square))
print()
print("Star")
print("----")
print(display_shelf(star))
print()
print("Heart")
print("-----")
print(display_shelf(heart))
print()
print("Moon")
print("----")
print(display_shelf(moon))
print()

book = input("Please insert a book name: ")
book = book.lower()

if not find_book(book, triangle) == -1:
    path = "ABE"
    number = find_book(book, triangle)
    shelf = "Triangle"
elif not find_book(book, circle) == -1:
    path = "ABCF"
    number = find_book(book, circle)
    shelf = "Circle"
elif not find_book(book, square) == -1:
    path = "ABCDG"
    number = find_book(book, square)
    shelf = "Square"
elif not find_book(book, star) == -1:
    path = "ABH"
    number = find_book(book, star)
    shelf = "Star"
elif not find_book(book, heart) == -1:
    path = "ABCI"
    number = find_book(book, heart)
    shelf = "Heart"
elif not find_book(book, moon) == -1:
    path = "ABCDJ"
    number = find_book(book, moon)
    shelf = "Moon"

print("Follow the path: " + path)

print("Once you have found the " + shelf + " shelf, the book will be on the " + str(humanize.ordinal(number[1] + 1)) + " row and it wil be the " + str(humanize.ordinal(number[1] + 1)) + " book")