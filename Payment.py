import sqlite3
import sys
import Main
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
    
    Confirm_Payment()


def Available_Product():
        connection = sqlite3.connect('SellerProduct.db')
        cursor = connection.cursor()

        cursor.execute('''SELECT productname,productprice,productcost,producttotalprice,sellername
        FROM Product 
        WHERE productquantity >= 1''')

        result = cursor.fetchall()

        print('\n',' '*20,'Available Products')
        print('| Product Name |  Price  |  Cost  | Total Price | Seller Name |')
        print('-'*63)
        for i in result:
            for x in i:
                print('|',i[0],' '*(11-len((str(i[0])))),'|',
                          i[1],' '*(6-len((str(i[1])))),'|',
                          i[2],' '*(5-len((str(i[2])))),'|',
                          i[3],' '*(10-len((str(i[3])))),'|',
                          i[4],' '*(10-len((str(i[4])))),'|')
                break
        print('\n')


def Confirm_Payment():
    connection = sqlite3.connect('usercart.db')
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