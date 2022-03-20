import Main
import os
import sys
import sqlite3
from datetime import datetime

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
                   productcost REAL NOT NULL,
                   producttotalprice REAL NOT NULL,
                   productproducedby TEXT NOT NULL,
                   productexpirydate DATETIME NOT NULL,
                   productquantity REAL NOT NULL,
                   productcatergory TEXT NOT NULL,
                   productenterdate DATETIME NOT NULL,
                   sellername TEXT NOT NULL)''')
    connection.commit()
    connection.close()

    Menu()

def Menu():
    print('')
    print('='*15,'Welcome',USERNAME,'='*15)
    print('\n1. Account Info\n2. Products\n3. Log Out')

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
    print('')
    print('='*15,'Account Info','='*15)
    print(f'Username: {USERNAME}')
    print(f'Password: {PWD}')
    print(f'Usertype: {USERTYPE}')

    print('\n1. Delete Account\n2. Change Account Info\n3. Back')
    option = int(input('\nChoose an option: '))
    while option != 1 and option !=2 and option !=3:
        option = int(input('Choose an option: '))
    
    if option == 1:
        Account_Del()
    elif option == 2:
        Account_Change()
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
    print('1. Change Username\n2. Change Password\n3. Back')
    option = int(input('\nChoose an option: '))
    while option!= 1 and option != 2 and option!= 3:
        option = int(input('Choose an option: '))
    
    if option == 1:
        Name_Change()
    elif option == 2:
        Pwd_Change()
    else:
        Account_Info()

def Name_Change():
    global USERNAME

    print('New Username')
    new_name = input('>> ')

    users = []
    with open('Files/Userdata.txt','r') as user:
        for i in user.readlines():
                i = i.strip().split(',')
                users.append(i)
        
        for i in users:
            if (USERNAME in i) and (PWD in i):
                userinfo = i
                users.remove(i)
        
        userinfo[0] = new_name
        users.append(userinfo)
    
    file = open('Files/Userdata.txt','w')
    file.close()

    with open('Files/Userdata.txt','a') as user:
        for i in users:
            name, password, utype = i
            user.write(f'{name},{password},{utype}\n')
    
    USERNAME = new_name
    print('Username Changed\n')

def Pwd_Change():
    global PWD

    print('New Password')
    new_pwd = input('>> ')

    users = []
    with open('Files/Userdata.txt','r') as user:
        for i in user.readlines():
                i = i.strip().split(',')
                users.append(i)
        
        for i in users:
            if (USERNAME in i) and (PWD in i):
                userinfo = i
                users.remove(i)
        
        userinfo[1] = new_pwd
        users.append(userinfo)
    
    file = open('Files/Userdata.txt','w')
    file.close()

    with open('Files/Userdata.txt','a') as user:
        for i in users:
            name, password, utype = i
            user.write(f'{name},{password},{utype}\n')
    
    PWD = new_pwd
    print('Password Changed\n')
    
    Account_Info()


#Seller Page
def Product_Page():
    print('')
    print('='*15,'Product Page','='*15)
    print("1. Create Product")
    print("2. Edit Product")
    print("3. Delete Product")
    print("4. View Own Product")
    print("5. Exit")
    
    option = int(input('\nChoose an option: '))
    while option != 1 and option !=2 and option !=3 and option !=4 and option !=5:
        option = int(input('Choose an option: '))
    
    if option == 1:
        Create_Product()
    elif option == 2:
        Edit_ProductInfo()
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
    productcost = productprice
    productproducedby = input('Enter where your product is produced: ')
    productexpirydate = input('Enter your product expiry date: yyyy-MM-dd')
    productquantity = input('Enter your product quantity: ')
    productcatergory = input('Enter your product catergory: Fruits or Herbs? ')
    productenterdate = (datetime.today().date())
    sellername = USERNAME
    producttotalprice = str(int(productprice)*int(productquantity))
    print(f'product name: "{productname}"')
    print(f'product price: RM "{productprice}"')
    print(f'product cost: RM "{productcost}"')
    print(f'product total price: RM "{producttotalprice}"')
    print(f'product producedby: "{productproducedby}"')
    print(f'product expirydate: "{productexpirydate}"')
    print(f'product quantity: "{productquantity}"')
    print(f'product catergory: "{productcatergory}"')
    print(f'product enter date: "{productenterdate}"')
    print(f'seller name: "{sellername}"')
    connection = sqlite3.connect('SellerProduct.db')
    cursor = connection.cursor()
    cursor.execute(f'INSERT INTO Product(productname,productprice,productcost,producttotalprice,\
                                         productproducedby,productexpirydate,productquantity,\
                                         productcatergory,productenterdate,sellername) \
                                         VALUES ("{productname}","{productprice}","{productcost}",\
                                         "{producttotalprice}","{productproducedby}","{productexpirydate}",\
                                         "{productquantity}","{productcatergory}","{productenterdate}","{sellername}")')
    connection.commit()
    connection.close()  
    print('Added successful.')
    Product_Page()


def Edit_ProductInfo():
    connection = sqlite3.connect('SellerProduct.db')
    cursor = connection.cursor()
    Seller_Products()
    productid = input('\nEnter the product id for the product you want to update: ')
    newproductname = input('Enter your product name: ')
    newproductprice = input('Enter your product price: ')
    newproductcost = input('Enter your product cost: ')
    newproducttotalprice = input('Enter your product total price: ')
    newproductproducedby = input('Enter where your product is produced: ')
    newproductexpirydate = input('Enter your product expiry date: yyyy-MM-dd HH:mm:ss ')
    newproductquantity = input('Enter your product quantity: ')
    newproductcatergory = input('Enter your product catergory: Fruits or Herbs? ')
    updateproduct = (f"UPDATE Product SET productname = '{newproductname}', productprice = {newproductprice},\
                       productcost = {newproductcost}, producttotalprice = {newproducttotalprice},\
                       productproducedby = '{newproductproducedby}', productexpirydate = '{newproductexpirydate}',\
                       productquantity = {newproductquantity}, productcatergory = '{newproductcatergory}' WHERE productid ={productid};")
    cursor.execute(updateproduct)
    connection.commit()
    connection.close()
    Product_Page()


def Delete_Product():
    connection = sqlite3.connect('SellerProduct.db')
    cursor = connection.cursor()
    Seller_Products()
    deleteid = input('\nEnter the id of product you want to delete: ') 
    deleteproduct = (f"DELETE from Product where productid = {deleteid}")
    cursor.execute('''SELECT * FROM Product''')
    cursor.execute(deleteproduct)
    connection.commit()
    connection.close()
    print('Product deleted.')
    Product_Page()


def Product_Viewing():
    Seller_Products()
    input('\nPress enter to return')
    Product_Page()

def Seller_Products():
    print('')
    print('='*15,'Seller\'s Products','='*15,'\n')

    connection = sqlite3.connect('SellerProduct.db')
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM Product WHERE sellername='{USERNAME}'")
    result = cursor.fetchall()

    print('| Product ID | Product Name | Price | Total Price |   Produce By   |      Expiry Date      | Quantity | Category |   Enter Date   | Seller Name |')
    print('-'*145)
    for i in result:
        for x in i:
            print('|',i[0],' '*(9-len((str(i[0])))),'|',
                    i[1],' '*(11-len((str(i[1])))),'|',
                    i[2],' '*(4-len((str(i[2])))),'|',
                    i[4],' '*(10-len((str(i[4])))),'|',
                    i[5],' '*(13-len((str(i[5])))),'|',
                    i[6],' '*(20-len((str(i[6])))),'|',
                    i[7],' '*(7-len((str(i[7])))),'|',
                    i[8],' '*(7-len((str(i[8])))),'|',
                    i[9],' '*(13-len((str(i[9])))),'|',
                    i[10],' '*(10-len((str(i[10])))),'|')
            break
    print('')