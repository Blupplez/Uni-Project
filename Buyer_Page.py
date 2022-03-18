import Main
import os
import sys
import sqlite3
import Shopping_Cart

USERNAME = None
PWD = None
USERTYPE = None

def Start(Username, Pwd):
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
    print('')
    print('='*15,'Welcome',USERNAME,'='*15)
    print('\n1. Account Info\n2. View Product\n3. Shopping Cart\n4. Log Out')

    option = int(input('\nChoose an option: '))
    while option != 1 and option !=2 and option !=3 and option !=4:
        option = int(input('Choose an option: '))
    
    if option == 1:
        Account_Info()
    elif option == 2:
        View_Product()
    elif option == 3:
        Shopping_Cart.Start(USERNAME ,PWD)
    else:
        Main.Access()



def Account_Info():
    print('')
    print('='*15,'Account Info','='*15)
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
    option = input('\nAre you sure you want to delete your account(Yes/No) ')
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

def View_Product():
    print ('\n1. New Product \n2. All Product \n3. Product Category \n4. Back')
    option = int(input('Choose an option: '))
    while option != 1 and option !=2 and option !=3 and option !=4:
        option = int(input('Choose an option: '))

    def New_Product():
        connection = sqlite3.connect('SellerProduct.db')
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM Product ORDER BY productid DESC LIMIT 3;''')
        result=cursor.fetchall()
        print ('Newest 3')
        for i in result:
            print (i)
        x=input('Press enter to return')
        View_Product()

    def All_Product():
        connection = sqlite3.connect('SellerProduct.db')
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM Product''')
        result=cursor.fetchall()
        for i in result:
            print (i)
        x=input('Press enter to return')
        View_Product()

    def Cat_Product():
        connection = sqlite3.connect('SellerProduct.db')
        cursor = connection.cursor()
        catergory = input('enter a catergory (Fruits or Herbs): ')
        cat = (f"'{catergory}'")
        catproductsearch = (f"SELECT * FROM Product where productcatergory={cat}")
        cursor.execute('''SELECT * FROM Product''')
        cursor.execute(catproductsearch)
        result=cursor.fetchall()
        for i in result:
            print(i)
        x=input('Press enter to return')
        View_Product()

    if option == 1:
        New_Product()
    elif option == 2:
        All_Product()
    elif option == 3:
        Cat_Product()
    else:
        Menu()