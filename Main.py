def get_credentials():
    global username
    global password

    username = input("Enter a username: ")
    password = input("Enter a password: ")


get_credentials()  # run the function

print(username, " ", password)  # Test

# Now directly from PyCharm