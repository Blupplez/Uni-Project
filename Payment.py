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
      if (Username in i) and (Pwd in i):  
            USERNAME = i[0]
      else:
            print('Error')
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