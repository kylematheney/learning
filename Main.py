def get_username():
    global username
    username = ''

    while username == '':
        username = input("Enter a username: ")
        if username == '':
            print("You have to enter a username.")


def get_password():
    global password
    password = ''

    while password == '':
        password = input("Enter a password (minimum 8 characters): ")
        if password == '':
            print("You have to enter a password.")
    validate_password(password)


def validate_password(pwd):
    is_valid = True  # This isn't a good idea
    check_pwd_len(pwd)


def check_pwd_len(pwd):
    return len(pwd) >= 8  # Returns "true" if password is 8+ characters


get_username()
get_password()


print(username, " ", password)
