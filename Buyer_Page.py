import Main
import os
import sys
import sqlite3
import Shopping_Cart

USERNAME = str
PWD = None
USERTYPE = str

def Start(Username, Pwd):
    global USERTYPE,USERNAME,PWD
    connection = sqlite3.connect('fruitsandherbs.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT username,password,usertype FROM userdata WHERE username='{Username}'")
    result = cursor.fetchall()
    print(result) 
    for i in result:
      if (Username in i[0]) and (Pwd in i[1]) and (USERTYPE in i[2]):  
            USERNAME = i[0]
            PWD = i[1]
            USERTYPE = i[2]
      else:
            print('Error')
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
    connection = sqlite3.connect('fruitsandherbs.db')
    cursor = connection.cursor()
    accountname = (f"'{USERNAME}'")
    checkinfo =(f"SELECT username,usertype,location,phonenumber FROM userdata where username={accountname}")
    cursor.execute(checkinfo)
    result=cursor.fetchall()
    print(result)
    connection.close()

    print('\n1. Delete Account\n2. Edit Info\n3.Back')
    option = int(input('\nChoose an option: '))
    while option != 1 and option !=2 and option !=3:
        option = int(input('Choose an option: '))
    
    if option == 1:
        Account_Del()
    elif option == 2:
        Edit_Info()
    else:
        Menu()


def Account_Del():
    option = input('\nAre you sure you want to delete your account(Yes/No) ')
    while option != 'Yes' and option != 'yes' and option != 'No' and option != 'no':
        option = input('(Yes/No) ')

    option = option.lower()

    if option == 'yes':
        connection = sqlite3.connect('fruitsandherbs.db')
        cursor = connection.cursor()
        accountname = (f"'{USERNAME}'")
        deleteaccount = (f"DELETE from userdata where username = {accountname}")
        cursor.execute('''SELECT * FROM userdata''')
        cursor.execute(deleteaccount)
        connection.commit()
        connection.close()
        Main.Access()
    elif option == 'no':
        Menu()
        
def Edit_Info():
    sellerpassword = input('Enter your new password')
    sellerlocation = input('Enter your new location: ')
    sellerphonenumber = input('Enter your new phone number: ')
    connection = sqlite3.connect('fruitsandherbs.db')
    cursor = connection.cursor()
    updateproduct = (f"UPDATE userdata SET password = '{sellerpassword}',location = '{sellerlocation}',\
                       phonenumber = '{sellerphonenumber}' WHERE username ={USERNAME};")
    cursor.execute(updateproduct)
    
    connection.commit()
    connection.close()
    Menu()

def View_Product():
    print ('\n1. New Product \n2. All Product \n3. Product Category \n4. Back')
    option = int(input('Choose an option: '))
    while option != 1 and option !=2 and option !=3 and option !=4:
        option = int(input('Choose an option: '))

    def New_Product():
        connection = sqlite3.connect('fruitsandherbs.db')
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM Product ORDER BY productid DESC LIMIT 3;''')
        result=cursor.fetchall()
        print (' '*60,'Newest 3 Products\n')
        print('| Product ID | Product Name |   Price   | Total Price |   Produce By   |      Expiry Date      | Quantity | Category |   Enter Date   | Seller Name |')
        print('-'*149)
        for i in result:
            for x in i:
                print('|',i[0],' '*(9-len((str(i[0])))),'|',
                    i[1],' '*(11-len((str(i[1])))),'|',
                    i[2],' '*(8-len((str(i[2])))),'|',
                    i[4],' '*(10-len((str(i[4])))),'|',
                    i[5],' '*(13-len((str(i[5])))),'|',
                    i[6],' '*(20-len((str(i[6])))),'|',
                    i[7],' '*(7-len((str(i[7])))),'|',
                    i[8],' '*(7-len((str(i[8])))),'|',
                    i[9],' '*(13-len((str(i[9])))),'|',
                    i[10],' '*(10-len((str(i[10])))),'|')
                break
        print('')
        input('Press ENTER to return')
        View_Product()

    def All_Product():
        connection = sqlite3.connect('fruitsandherbs.db')
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM Product")
        result = cursor.fetchall()

        print('\n',' '*65,'All Products\n')
        print('| Product ID | Product Name |   Price   | Total Price |   Produce By   |      Expiry Date      | Quantity | Category |   Enter Date   | Seller Name |')
        print('-'*149)
        for i in result:
            for x in i:
                print('|',i[0],' '*(9-len((str(i[0])))),'|',
                    i[1],' '*(11-len((str(i[1])))),'|',
                    i[2],' '*(8-len((str(i[2])))),'|',
                    i[4],' '*(10-len((str(i[4])))),'|',
                    i[5],' '*(13-len((str(i[5])))),'|',
                    i[6],' '*(20-len((str(i[6])))),'|',
                    i[7],' '*(7-len((str(i[7])))),'|',
                    i[8],' '*(7-len((str(i[8])))),'|',
                    i[9],' '*(13-len((str(i[9])))),'|',
                    i[10],' '*(10-len((str(i[10])))),'|')
                break
        print('')
        input('Press ENTER to return')
        View_Product()

    def Cat_Product():
        connection = sqlite3.connect('fruitsandherbs.db')
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