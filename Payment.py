'''
********** ********** ********** ********** **********
Code Filename: Payment.py
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

import sqlite3
import sys
import Main
import Shopping_Cart

USERNAME = None

def Start(Username, Pwd):
    global USERNAME
    connection = sqlite3.connect('fruitsandherbs.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM userdata WHERE username='{Username}'")
    result = cursor.fetchall()
    for i in result:
        USERNAME = i[0]
    Confirm_Payment()


def Available_Product():
        connection = sqlite3.connect('fruitsandherbs.db')
        cursor = connection.cursor()

        cursor.execute('''SELECT *
        FROM Product 
        WHERE productquantity >= 1''')

        result = cursor.fetchall()

        print('\n',' '*20,'Available Products')
        print('| Product Name |  Price  |  Cost  | Total Price | Seller Name |')
        print('-'*63)
        for i in result:
            for x in i:
                print('|',i[1],' '*(11-len((str(i[1])))),'|',
                          i[2],' '*(6-len((str(i[2])))),'|',
                          i[3],' '*(5-len((str(i[3])))),'|',
                          i[4],' '*(10-len((str(i[4])))),'|',
                          i[10],' '*(10-len((str(i[10])))),'|')
                break
        print('\n')


def Confirm_Payment():
    print(USERNAME)
    connection = sqlite3.connect('fruitsandherbs.db')
    cursor = connection.cursor()
    # Show Shopping Cart Before Payment
    print('\n','='*15,'Your Shopping Cart','='*15)
    Shopping_Cart.Print_Cart()
    urusername = USERNAME

    # Show Available Products
    print('\nHere are some other products you may want to buy.')
    Available_Product()
    print('1. Continue Shopping\n2. Continue Payment')
    option = int(input('\nChoose an option: '))
    while option != 1 and option !=2:
        option = int(input('Choose an option: '))
    
    if option == 1:
        Shopping_Cart.Shopping_Menu()

    cursor.execute(f"SELECT SUM(producttotalprice) FROM usercart WHERE username='{urusername}'")
    print('The total price for your checkout is')
    print(cursor.fetchone()[0])
    print('Purchases Completed')
    cursor.execute(f"DELETE FROM usercart WHERE username='{urusername}'")
    connection.commit()
    connection.close()
    Shopping_Cart.Shopping_Menu()