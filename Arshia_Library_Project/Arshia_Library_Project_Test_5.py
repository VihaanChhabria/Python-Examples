import humanize
import numpy as np
import cv2

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

cap = cv2.VideoCapture(0) #Gets video.

def find_book(book, list_name):
    for shelf_row in list_name:
        if book in shelf_row:
            inner = shelf_row.index(book)
            outer = list_name.index(shelf_row)
            return inner, outer
    return -1

def display_2shelf(list_name1,list_name2):
    list_Count = len(list_name1)
    list_Ctr = 0

    while (list_Ctr < list_Count):

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


        list_Ctr = list_Ctr + 1
        row_books = row_books1 + row_books2
        print(colored(0,191,255, row_books))

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

print(colored(0,191,255, 'Hello, World'))



print(colored(255, 165, 0, "-------------------------------------------------------------------------------------------------------------------------"))
print(colored(123, 104, 238, "Triangle                                                    Circle\n"))
print(colored(27, 27, 27, display_2shelf(triangle, circle)))
print(colored(255, 165, 0, "-------------------------------------------------------------------------------------------------------------------------\n"))

print(colored(255, 165, 0, "-------------------------------------------------------------------------------------------------------------------------"))
print(colored(123, 104, 238, "Square                                                      Star\n"))
print(colored(27, 27, 27, display_2shelf(square, star)))
print(colored(255, 165, 0, "-------------------------------------------------------------------------------------------------------------------------\n"))

print(colored(255, 165, 0, "-------------------------------------------------------------------------------------------------------------------------"))
print(colored(123, 104, 238, "Heart                                                       Moon\n"))
print(colored(27, 27, 27, display_2shelf(heart, moon)))
print(colored(255, 165, 0, "-------------------------------------------------------------------------------------------------------------------------\n"))

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

if not find_book(book, triangle) == -1:
    while True:
        ret, frame = cap.read() #This will take the dimensions of the camera with the varible frame.
        width = int(cap.get(3)) #This will get the width of the camera.
        height = int(cap.get(4)) #This will get the hieght of the camera.

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #Converts the video into bgr.

        green_lower = (49,70,71)
        green_upper = (102, 255, 255)

        lower = np.array([green_lower]) #Where the program starts seeing color
        upper = np.array([green_upper]) #Where the program does not see the color

        mask = cv2.inRange(hsv, lower, upper) #Impiments the ranges to the frame

        kernel = np.ones((8,8),np.uint8)

        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

        result = cv2.bitwise_and(frame, frame, mask = mask)

        contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        output = cv2.drawContours(result, contours, -1, (0, 0, 255), 3)

        cv2.imshow('frame', result)
        cv2.imshow('mask', mask)

        if cv2.waitKey(1) == ord('q'): #This will close the program with the letter q.
            break
    cap.release()
    cv2.destroyAllWindows()