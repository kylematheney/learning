file = open("definitelynotapassword.txt", "w+")  # 'w' = write, '+' = create file if it doesn't exist


def get_username():
    global username
    username = ''

    while username == '':
        username = input("Enter a username: ")
        if username == '':
            print("You have to enter a username.")
    file.write("USER="+username)


def get_password():
    global password
    password = ''

    while password == '':
        password = input("Enter a password (minimum 8 characters): ")
        if password == '':
            print("You have to enter a password.")
    file.write("\nPASS="+password)


get_username()
get_password()
file.close()

print(username, " ", password)
