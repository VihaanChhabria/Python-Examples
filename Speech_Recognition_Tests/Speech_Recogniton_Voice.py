from Speech_Recognition_Functions import * #Gets Functions

while True:
    s = speech() #Sees what speaker is saying

    print(s) #Prints what what speaker is saying

    if s == "my dude": #If the speaker says "my dude" (name of code)
        print("Recognized")

        s = options_dir() #Starts bringing up options
        print(s)
        options(s)