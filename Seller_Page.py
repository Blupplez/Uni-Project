import Main
import os
import sys
import sqlite3

USERNAME = None
PWD = None
USERTYPE = None

#create database if not exist
connection = sqlite3.connect('SellerProduct.db')
cursor = connection.cursor()


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
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Product(
                productid INTEGER PRIMARY KEY,
                productname TEXT NOT NULL,
                productprice REAL NOT NULL,
                productproducedby TEXT NOT NULL,
                productexpirydate TEXT NOT NULL,
                productquantity REAL NOT NULL,
                productcatergory REAL NOT NULL,
                sellername TEXT NOT NULL)''')
    connection.commit()
    connection.close()

    Menu()


def Menu():
    print(f'\nWelcome {USERNAME}')
    print('\n1.Account Info\n2.Products\n3.Log Out')

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
    print('\nAccount Info')
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


def Account_Change():
    pass


#Seller Page
def Product_Page():
    print("1. Create Product")
    print("2. Edit Product")
    print("3. Delete Product")
    print("4. View Product")
    print("5. Exit")
    
    option = int(input('\nChoose an option: '))
    while option != 1 and option !=2 and option !=3:
        option = int(input('Choose an option: '))
    
    if option == 1:
        Create_Product()
    elif option == 2:
        Edit_Product()
    elif option == 3:
        Delete_Product()
    elif option == 4:
        Product_Viewing()
    else:
        Menu()


#Add new product to database
def Create_Product():
    productname = input('Enter your product name: ')
    productprice = input('Enter your product price: ')
    productproducedby = input('Enter where your product is produced: ')
    productexpirydate = input('Enter your product expiry date: ')
    productquantity = input('Enter your product quantity: ')
    productcatergory = input('Enter your product catergory: ')
    sellername = input('Enter your seller name: ')
    connection = sqlite3.connect('SellerProduct.db')
    cursor = connection.cursor()
    cursor.execute(f'INSERT INTO Product(productname,productprice,productproducedby,productexpirydate,productquantity,productcatergory,sellername) VALUES ("{productname}","{productprice}","{productproducedby}","{productexpirydate}","{productquantity}","{productcatergory}","{sellername}")')
    connection.commit()
    connection.close()
    Product_Page()


def Edit_Product():
    pass


def Delete_Product():
    pass


def Product_Viewing():
    print('1. Show Product')
    print('2. Show New Products')
    print('3. Show All Products')
    print('4. Show Product by Catergory')
    print('5. Back')

    
    #Show Own Product
    def Own_Product():
        cursor.execute('''SELECT productname,sellername FROM Product''')
        result=cursor.fetchall()
        print(result)
        for i in result:
            print(i)
        connection.close()
    

    #Show New Product
    def New_Product():
        cursor.execute(''' ''')


    #Show All Product
    def All_Product():
        cursor.execute('''SELECT productname,sellername FROM Product''')
        result = cursor.fetchall()
        print(result)


    #Show Product in Catergory
    def Cat_Product():
        cursor.execute(''' ''')


    option = int(input('Choose an option: '))
    if option == 1:
        Own_Product()
    elif option == 2:
        New_Product()
    elif option == 3:
        All_Product()
    elif option == 4:
        Cat_Product()
    else:
        Product_Page()
