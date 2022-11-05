def head():
  print("               ----------")
  print("               |        |")
  print("               |        |")
  print("               |        |")
  print("               |        |")
  print("               ----------")
  print("                    |")
def body():
  print("               ----------")
  print("               |        |")
  print("               |        |")
  print("               |        |")
  print("               |        |")
  print("               |        |")
  print("               |        |")
  print("               |        |")
  print("               ----------")
def body_arms():
  print("               ----------")
  print("               |        |")
  print("               |        |")
  print("---------------|        |---------------")
  print("               |        |")
  print("               |        |")
  print("               |        |")
  print("               |        |")
  print("               ----------")
def legs():
  print("               |        |")
  print("               |        |")
  print("               |        |")
  print("               |        |")
  print("               |        |")
  print("               |        |")
def maker(wrong, word):
  if wrong == 1:
    head()
  if wrong == 2:
    head()
    body()
  if wrong == 3:
    head()
    body_arms()
  if wrong == 4:
    head()
    body_arms()
    legs()
def clear_consle():
    consle_clear_counter = 0
    while consle_clear_counter < 100:
        print("\n")
        consle_clear_counter = consle_clear_counter + 1

import random
import enchant



d = enchant.Dict("en_US")

words = ("gold", "possible", "plane", "age", "dry", "wonder", "laugh")

wrong = 0

word = words[random.randint(0, len(words) - 1)]
word_lenght = len(word)
word_blank = ""
word_list = list(word)
count = 0

while count < word_lenght:
    word_blank = word_blank + "_ "
    count = count + 1

while True:
    print(word_blank)

    g = input()
    g = g.lower()

    if True:#(len(g) == len(word)) and (d.check(g)):
        clear_consle()
        for letter_counter in word_list:
            if g in word_list:
                finder = word_list.index(g)
                count = 0
                while count < word_lenght:
                    word_blank = word_blank + "_ "
                    count = count + 1
                    if count == finder - 1:
                        word_blank = word_blank + g + " "
        if g == word:
            print("You guessed the word!")
        else:
            print("Wrong! Try again!")
            wrong = wrong + 1
            maker(wrong, word)
            #
            if wrong > 4:
                print("You ran out of tries! The word was " + word + "!")
                break
    else:
        print("Please enter a word with " + str(len(word)) + " letters and that is part of the english dictonary.")