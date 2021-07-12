#A bank to write stuff in
while True:
    choice = input("1 to Sign Up, 2 to Sign In ")

    if choice == "1":
        print("Creating Account!")
        username = input("Whats The Username To Set?")
        password = input("Whats The Password To Set?")
        U_accountpersonal = open("Username.txt", "w")
        U_accountpersonal.write(username)
        P_accountpersonal = open("Password.txt", "w")
        P_accountpersonal.write(password)
        continue

    if choice == "2":
        usernamecheck = input("Whats The Username?")
        passwordcheck = input("Whats The Password?")
        if not usernamecheck == U_accountpersonal.read() or not passwordcheck == P_accountpersonal.read():
            print("wrong")
            continue
        if usernamecheck == U_accountpersonal.read() and passwordcheck == P_accountpersonal.read():
            f = open("Account.txt", "r")
            print(f.read())
            if f.read() == "":
                print("You have nothing in your account!")

            choicetext = input("Press 1 to Delete Everything, Press 2 to Add Stuff, Press 3 to Rename Password or Username, 4 to Delete Account")

            if choicetext == "1":
                f = open("Account.txt", "w")
                f.write("")
                continue
            
            if choicetext == "2":
                f = open("Account.txt", "a")
                f.write()