triangle = ["harry potter", "ignite me", "the libray of lost things", "american royals", "cinder", "stiff"]
circle = ["eleven", "give and take","give and take", "black out", "one last stop", "fire with fire"]
square = ["chosen", "tweet cute", "infinity son", "midnight sun", "if we were us" ,"camp"]
star = ["boys dont knit", "smile", "drama", "idetical", "crank" ,"pawn"]
heart = ["crossover ","everything everthing" ,"refuge","red queen" ,"the book theif","if i stay"]
moon = ["heros", "tenderness" , "girl in peices ", "wonder", "sheets", "they both die in the end"]

bin_triangle = True
bin_circle = True
bin_square = True
bin_star = True
bin_heart = True
bin_moon = True

path = "Book Not Found"

def find_book(book, list_name):
    return_flag = True
    try:
        list_name.index(book)
    except:
        return_flag = False
    return return_flag

book = input("Please insert a book name: ")
book = book.lower()

if find_book(book, triangle):
    path = "ABE"
elif find_book(book, circle):
    path = "ABCF"
elif find_book(book, square):
    path = "ABCDG"
elif find_book(book, star):
    path = "ABH"
elif find_book(book, heart):
    path = "ABCI"
elif find_book(book, moon):
    path = "ABCDJ"

print("Follow the path: " + path)

