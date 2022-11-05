#Password Check
while True:
    password = input("What is the password? ")
    if password == '12':
        print("Login Successful!")

    if password != '12':
        print("Wrong!")

    if password == 'exit':
        exit()
exit()