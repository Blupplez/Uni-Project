import Main
import os
import sys
import sqlite3

USERNAME = None
PWD = None
USERTYPE = None

connection = sqlite3.connect('SellerProduct.db')
cursor = connection.cursor()

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
    Clear()
    print(f'Welcome {USERNAME}')
    print('\n1.Account Info\n2.View Product\n3.Exit')

    option = int(input('\nChoose an option: '))
    while option != 1 and option !=2 and option !=3:
        option = int(input('Choose an option: '))
    
    if option == 1:
        Account_Info()
    elif option == 2:
        View_Product()
    else:
        Main.Access()


def Account_Info():
    Clear()
    print(f'Username: {USERNAME}')
    print(f'Password: {PWD}')
    print(f'Usertype: {USERTYPE}')

    print('\n1. Delete Account\n2. Back')
    option = int(input('\nChoose an option: '))
    while option != 1 and option !=2:
        option = int(input('Choose an option: '))
    
    if option == 1:
        Account_Del()
    else:
        Menu()


def Account_Del():
    Clear()
    option = input('Are you sure you want to delete your account(Yes/No) ')
    while option != 'Yes' and option != 'yes' and option != 'No' and option != 'no':
        option = input('(Yes/No) ')

    option = option.lower()

    users = []
    if option == 'yes':
        with open('Files/Userdata.txt','r') as user:
            for i in user.readlines():
                i = i.strip().split(',')
                users.append(i)
        
        for i in users:
            if (USERNAME in i) and (PWD in i):
                users.remove(i)
        
        file = open('Files/Userdata.txt','w')
        file.close()

        with open('Files/Userdata.txt','a') as user:
            for i in users:
                name, password, utype = i
                user.write(f'{name},{password},{utype}\n')
        
        Main.Access()
    elif option == 'no':
        Menu()


def Account_Change():
    pass

def View_Product():
    print ('\n1.New Product \n2.All Product \n3.Product Category')
    option = int(input('Choose an option: '))
    def New_Product():
        pass

    def All_Product():
        connection = sqlite3.connect('SellerProduct.db')
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM Product''')
        result=cursor.fetchall()
        print(result)

    def Cat_Product():
        pass

    if option == 1:
        New_Product()
    elif option == 2:
        All_Product()
    else:
        Cat_Product()


# Clear CMD
def Clear():
    os.system('cls')