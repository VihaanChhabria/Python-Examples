#Hangman Game
import random

a = ["rction" , "hn", "schl", "hll", "ppr", "tn", "flwr", "mgntc", "ctps"]
b = (random.choice(a))
counter = 0
LivesLeft = 3

while counter < 3 :

    print("Random Word",b)
    c = input("type in the missing vowels(in lower case) ")

    if ((c == "eaio") or (c == "e") or (c == "oo") or (c == "i") or (c == "ae") or (c == "e") or (c == "oe") or (c == "aei") or (c =="oou")):
        print("correct")
        b = (random.choice(a))
    else :
        counter = counter + 1
        LivesLeft = LivesLeft - counter
        print("Lives left",LivesLeft)