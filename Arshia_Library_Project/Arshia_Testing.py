from bottle import get, post, request, run # or route
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

def find_book(book, list_name):
    for shelf_row in list_name:
        if book in shelf_row:
            inner = shelf_row.index(book)
            outer = list_name.index(shelf_row)
            return inner, outer
    return -1

def display_multiple_shelf(list_name1, list_name2):

    list_Count = len(list_name1)
    list_Ctr = 0
    togeter = ""

    while (list_Ctr < list_Count):
        row_record = display_2shelf(list_name1, list_name2, list_Ctr)
        togeter = togeter + row_record
        list_Ctr = list_Ctr + 1
        print(row_record)


def display_2shelf(list_name1, list_name2, list_Ctr):

        shelf_row = list_name1[list_Ctr]
        row_books1 = ""
        for shelf_col in shelf_row:
            num_space_char = max_book_len - len(shelf_col) + 5
            space_char = ""
            counter = 0
            while counter <= num_space_char:
                space_char = space_char + " "
                counter = counter + 1
            row_books1 = row_books1 + shelf_col + space_char

        shelf_row = list_name2[list_Ctr]
        row_books2 = ""
        for shelf_col in shelf_row:
            num_space_char = max_book_len - len(shelf_col) + 5
            space_char = ""
            counter = 0
            while counter <= num_space_char:
                space_char = space_char + " "
                counter = counter + 1
            row_books2 = row_books2 + shelf_col + space_char

        row_books = row_books1 + row_books2
        return(row_books)

@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Book: <input name="book" type="text" />
            <input value="Enter" type="submit" />
        </form>
    ''', "<p>-------------------------------------------------------------------------------------------------------------------------</p>", "<p>" + display_2shelf(triangle, circle, 0) + "</p>", "<p>" + display_2shelf(triangle, circle, 1) + "</p>", "<p>" + display_2shelf(triangle, circle, 2) + "</p>"

@post('/login') # or @route('/login', method='POST')
def do_login():
    book = request.forms.get('book')
    book = book.lower()

    #if (book == "username"):
    #    return "<p>Your login information was correct.</p>"
    #else:
    #    return "<p>Login failed.</p>"

    path = ""
    number = ""
    shelf = ""

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
    
    a = "Follow the path: " + path + "."
    b = "Once you have found the " + shelf + " shelf, the book will be on the " + str(humanize.ordinal(number[1] + 1)) + " row and it will be the " + str(humanize.ordinal(number[1] + 1)) + " book."
    return a, b

    

run(host='localhost', port=8080, debug=True)