import Main
import os
import sys
import sqlite3

USERNAME = None
PWD = None
USERTYPE = None

connection = sqlite3.connect('SellerProduct.db')
cursor = connection.cursor()

#create database if not exist
cursor.execute('''CREATE TABLE IF NOT EXISTS Product(
                productid INTEGER PRIMARY KEY,
                productname TEXT NOT NULL,
                productprice REAL NOT NULL,
                productproducedby TEXT NOT NULL,
                productexpirydate TEXT NOT NULL,
                productquantity REAL NOT NULL,
                sellername TEXT NOT NULL)''')
connection.commit()
connection.close()

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
    print('\n1.Account Info\n2.Products\n3.Exit')

    option = int(input('\nChoose an option: '))
    while option != 1 and option != 2 and option != 3:
        option = int(input('Choose an option: '))
    
    if option == 1:
        Account_Info()
    elif option == 2:
        Product_Page()
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


#Seller Page
def Product_Page():
    print("1. Create Product")
    print("2. Edit Product")
    print("3. Delete Product")
    print("4. Exit")
    
    option = int(input('\nChoose an option: '))
    while option != 1 and option !=2 and option !=3:
        option = int(input('Choose an option: '))
    
    if option == 1:
        Create_Product()
    elif option == 2:
        Edit_Product()
    elif option == 3:
        Delete_Product()
    else:
        Menu()

#Add new product to database
def Create_Product():
    productname = input('Enter your product name: ')
    productprice = input('Enter your product price: ')
    productproducedby = input('Enter where your product is produced: ')
    productexpirydate = input('Enter your product expiry date: ')
    productquantity = input('Enter your product quantity: ')
    sellername = input('Enter your seller name: ')
    cursor.execute(f'INSERT INTO Product(productname,productprice,productproducedby,productexpirydate,productquantity,sellername) VALUES ("{productname}","{productprice}","{productproducedby}","{productexpirydate}","{productquantity}","{sellername}")')
    connection.commit()
    connection.close()
    Product_Page()


def Edit_Product():
    pass


def Delete_Product():
    pass


# Clear CMD
def Clear():
    os.system('cls')
