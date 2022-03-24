'''
********** ********** ********** ********** **********
Code Filename: Buyer_Page.py
Course: PSP0201 Mini IT Project 
Trimester: 2120
Lecture Section: TC1V
Tutorial Section: TL1V

Student Name as per MMU 1: Imran Syahmi bin Shahridan
Student ID 1: 1201103195
Email 1: 1201103195@student.mmu.edu.my

Student Name as per MMU 2: Chua Kee Ray
Student ID 2: 1201103232
Email 2: 1201103232@student.mmu.edu.my

Student Name as per MMU 3: Tan Swee jen
Student ID 3: 1201103464
Email 3: 1201103464@student.mmu.edu.my

Student Name as per MMU 4: Ng Zhi Yang
Student ID 4: 1201103665
Email 4: 1201103665@student.mmu.edu.my
********** ********** ********** ********** **********
'''

import Main
import os
import sys
import sqlite3
import Shopping_Cart

USERNAME = None
PWD = None

def Start(Username, Pwd):
    global USERNAME,PWD
    connection = sqlite3.connect('fruitsandherbs.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM userdata WHERE username='{Username}'")
    result = cursor.fetchall()
    for i in result:
      if (Username in i) and (Pwd in i):  
            USERNAME = i[0]
            PWD = i[1]
      else:
            print('Error')
    Menu()


def Menu():
    Username = USERNAME
    Pwd = PWD
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
        Shopping_Cart.Start(Username,Pwd)
    else:
        Main.Access()


def Account_Info():
    print('')
    print('='*15,'Account Info','='*15)
    connection = sqlite3.connect('fruitsandherbs.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM userdata WHERE username='{USERNAME}'")
    result = cursor.fetchall()
    print(result)
    connection.close()

    print('\n1. Delete Account\n2. Edit Info\n3. Back')
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

    if option == 'yes':
        connection = sqlite3.connect('fruitsandherbs.db')
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM userdata''')
        cursor.execute(f"DELETE from userdata WHERE username ='{USERNAME}'")
        connection.commit()
        connection.close()
        Main.Access()
    elif option == 'no':
        Menu()


def Account_Change():
    print('')
    print('='*15,'Edit Info','='*15)
    print('\n1. Change Username\n2. Change Password\n3. Back')
    option = int(input('\nChoose an option: '))
    while option!= 1 and option != 2 and option!= 3:
        option = int(input('Choose an option: '))
    
    if option == 1:
        Change_Name()
    elif option == 2:
        Change_Pwd()
    else:
        Account_Info()


def Change_Pwd():
    print('\nEnter your new password')
    new_pwd = input('>> ')
    connection = sqlite3.connect('fruitsandherbs.db')
    cursor = connection.cursor()
    cursor.execute(f"UPDATE userdata SET password = '{new_pwd}' WHERE username = '{USERNAME}'")
    connection.commit()
    connection.close()
    Account_Info()


def Change_Name():
    global USERNAME
    print('\nEnter your new username')
    new_name = input('>> ')
    connection = sqlite3.connect('fruitsandherbs.db')
    cursor = connection.cursor()
    cursor.execute(f"UPDATE userdata SET username = '{new_name}' WHERE username = '{USERNAME}'")
    connection.commit()
    connection.close()
    USERNAME = new_name
    Account_Info()


def View_Product():
    print('')
    print('='*15,'Product Page','='*15)
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

        print('\n1. Fruits\n2. Herbs')
        option = input('>> ')
        if option == 1:
            cat = 'Fruits'
        else:
            cat = 'Herbs'

        cursor.execute(f"SELECT * FROM Product where productcatergory='{cat}'")
        result = cursor.fetchall()
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
        input('Press enter to return')
        View_Product()

    if option == 1:
        New_Product()
    elif option == 2:
        All_Product()
    elif option == 3:
        Cat_Product()
    else:
        Menu()