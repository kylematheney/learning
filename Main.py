def get_username():
    global username
    username = input("Enter a username: ")


def get_password():
    global password
    password = input("Enter a password: ")


get_username()
get_password()

print(username, " ", password)  # Test

#Testing changes