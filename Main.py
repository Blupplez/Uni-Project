'''
********** ********** ********** ********** **********
Code Filename: Main.py
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

import os
import sys
import Buyer_Page
import Seller_Page

# Opens Login & Sign In Page
def Access():
    print('')
    print('='*15,'Fruits & Herbs Shop','='*15)
    print('1. Login\n2. Create New Account\n3. Exit')

    option = int(input('\nChoose an option: '))
    while option != 1 and option !=2 and option !=3:
        option = int(input('Choose an option: '))
    
    if option == 1:
        Login()
    elif option == 2:
        Sign_Up()
    else:
        sys.exit()


# Sign in Page
def Sign_Up():
    print('')
    print('='*15,'Sign Up','='*15)
    Username = input('\nUsername: ')
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
    print('')
    print('='*15,'Login','='*15)
    while Access == False:
        Username = input('\nUsername: ')
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


# Run the program
if __name__ == "__main__":
    Access()