import Main
import os

USERNAME = None
PWD = None
USERTYPE = None

def Start(Username, Pwd):
    Clear()
    global USERTYPE,USERNAME,PWD
    with open('Files/Userdata.txt','r') as user:
        for users in user.readlines():
            i = users.strip().split(',')
            if (Username in i) and (Pwd in i):
                Name, Password, UserType = i
                USERNAME = Name
                PWD = Password
                USERTYPE = UserType
    Menu()

def Menu():
    print(f'Welcome {USERNAME}')
    print('\n1.Exit')

    option = int(input('\nChoose an option: '))
    while option != 1:
        option = int(input('Choose an option: '))
    
    if option == 1:
        Main.Access()

# Clear CMD
def Clear():
    os.system('cls')