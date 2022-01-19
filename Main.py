import os
import sys
import Buyer_Page
import Seller_Page

# Opens Login & Sign In Page
def Access():
    Clear()
    print('Welcome User')
    print('1. Login\n2. Sign In\n3. Exit')

    option = int(input('\nChoose an option: '))
    while option != 1 and option !=2 and option !=3:
        option = int(input('Choose an option: '))
    
    if option == 1:
        Clear()
        Login()
    elif option == 2:
        Clear()
        Sign_In()
    else:
        sys.exit()


# Sign in Page
def Sign_In():
    print('Sign In')
    Username = input('Username: ')
    Pwd = input('Password: ')
    print('\n1. Buyer\n2. Seller')
    option = int(input('\nChoose an option: '))
    while option != 1 and option !=2:
        option = int(input('Choose an option: '))
    
    if option == 1:
        User_Type = 'buyer'
    else:
        User_Type = 'seller'

    with open('Files/Userdata.txt','a') as user:
        user.write(f'{Username},{Pwd},{User_Type}\n')
    
    if User_Type == 'buyer':
        Buyer_Page.Start(Username, Pwd)
    else:
        Seller_Page.Start(Username, Pwd)

# Login Page
def Login():
    Access = False

    while Access == False:
        print('Login')
        Username = input('Username: ')
        Pwd = input('Password: ')

        with open('Files/Userdata.txt','r') as user:
            for users in user.readlines():
                i = users.strip().split(',')
                if (Username in i) and (Pwd in i):
                    name, password, usertype = i
                    Access = True
                    if usertype == 'buyer':
                        Buyer_Page.Start(Username, Pwd)
                    elif usertype == 'seller':
                        Seller_Page.Start(Username, Pwd)
                else:
                    Access = False
    

# Clear CMD
def Clear():
    os.system('cls')


# Run the program
if __name__ == "__main__":
    Access()