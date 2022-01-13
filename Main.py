import os
import sys

# Opens Login & Sign In Page
def Access():
    Clear()
    print('Welcome User')
    print('1. Login\n2. Sign In\n3. Exit')

    option = int(input('\nChoose an option: '))
    while option != 1 and option !=2 and option !=3:
        option = int(input('Choose an option: '))
    
    if option == 1:
        Login()
    elif option == 2:
        Sign_In()
    else:
        sys.exit()


# Sign in Page
def Sign_In():
    print('Sign In')


# Login Page
def Login():
    print('Login')


# Clear CMD
def Clear():
    os.system('cls')


# Run the program
if __name__ == "__main__":
    Access()