import sqlite3
import sys
import Main
import Payment
import Buyer_Page

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
    Shopping_Menu()

#Create a Shopping Cart for user
connection = sqlite3.connect("usercart.db")
cursor = connection.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS usercart(
                rowid INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                productid INTEGER NOT NULL,
                productname TEXT NOT NULL,
                productprice REAL NOT NULL,
                productquantity INTERGER NOT NULL,
                productproducedby TEXT NOT NULL,
                productexpirydate TEXT NOT NULL,
                producttotalprice TEXT NOT NULL,
                sellerinformation TEXT NOT NULL)''')

connection.commit()
connection.close()

#Print Out for User
def Print_Cart():
    connection = sqlite3.connect('usercart.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM usercart WHERE username='{USERNAME}'")
    result = cursor.fetchall()

    # Checks if there is items in shopping cart
    items = 0
    for i in result:
        items+=1
    
    if items == 0:
        print('\nEmpty Shopping Cart')
        input('Press ENTER to go back to shopping')
        Shopping_Menu()
    else:
        pass

    # Shows shopping cart
    print('\n',' '*56,'Shopping Cart')
    print(' '*56,'-'*15)
    print('| Row ID |   Username   | Product ID |   Product Name   |  Price  | Quantity |  Produced By  |      Expiry Date      | Total Price | Seller Name |')
    print('-'*136)
    for i in result:
        for x in i:
                print('|',i[0],' '*(5-len((str(i[0])))),'|',
                          i[1],' '*(11-len((str(i[1])))),'|',
                          i[2],' '*(9-len((str(i[2])))),'|',
                          i[3],' '*(15-len((str(i[3])))),'|',
                          i[4],' '*(6-len((str(i[4])))),'|',
                          i[5],' '*(7-len((str(i[5])))),'|',
                          i[6],' '*(12-len((str(i[6])))),'|',
                          i[7],' '*(20-len((str(i[7])))),'|',
                          i[8],' '*(10-len((str(i[8])))),'|',
                          i[9],' '*(10-len((str(i[9])))),'|')
                break
    connection.commit()
    connection.close()

#Print All Product for User
def Print_Product():
    connection = sqlite3.connect('SellerProduct.db')
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM Product''')
    output = cursor.fetchall()
    result = [i[0] for i in cursor.description]
    print(result)
    for value in output:
     print(value)
    connection.close()


#Select Option from User
def Shopping_Menu():
    print('')
    print('='*15,f'{USERNAME}\'s Shopping Cart','='*15)
    print("1. Select or Add Product into Shopping Cart")
    print("2. Edit Product in Shopping Cart")
    print("3. Delete Product in Shopping Cart")
    print("4. Proceed to Payment")
    print("5. Back")


    option = int(input('\nChoose an option: '))
    while option != 1 and option !=2 and option !=3 and option !=4 and option !=5:
        option = int(input('Choose an option: '))

    if option == 1:
        Add_Product()
    elif option == 2:
        Edit_Product()
    elif option == 3:
        Delete_Product()
    elif option == 4:
        Proceed_Payment()
    else:
        Buyer_Page.Menu()



#Add Product for User
def Add_Product():
    Print_Product()
    connection = sqlite3.connect('SellerProduct.db')
    cursor = connection.cursor()

    username = USERNAME
    productid = input('Enter the product id: ')
    print('How much would you want to buy?')
    productquantity = input('>> ')
    
    cursor.execute(f"SELECT * FROM Product WHERE productid='{productid}'")
    result = cursor.fetchall()

    for i in result:
        for x in i:
            productname = i[1]
            productprice = i[2]
            productproducedby = i[5]
            productexpirydate = i[6]
            producttotalprice = str(int(productprice)*int(productquantity))
            sellerinformation = i[10]

    connection = sqlite3.connect('usercart.db')
    cursor = connection.cursor()
    cursor.execute(f'INSERT INTO usercart(username, productid, productname, productprice, productquantity,\
                     productproducedby, productexpirydate, producttotalprice,sellerinformation) \
                     VALUES ("{username}","{productid}","{productname}","{productprice}","{productquantity}",\
                     "{productproducedby}","{productexpirydate}","{producttotalprice}","{sellerinformation}")')
    connection.commit()
    connection.close()
    print('Product successfully added into cart')
    Shopping_Menu()




#Edit Product for User 
def Edit_Product():
    connection = sqlite3.connect('usercart.db')
    cursor = connection.cursor()
    Print_Cart()
    therowid = input('Enter the row id of the product: ')
    quantitychange = input('Enter the new quantity of the product you would like to change: ')

    cursor.execute(f"SELECT * FROM usercart WHERE productid='{therowid}'")
    result = cursor.fetchall()

    for i in result:
        for x in i:
            newprice = str(int(i[3])*int(quantitychange))

    cursor.execute(f"UPDATE usercart SET productquantity='{quantitychange}' WHERE rowid='{therowid}'")
    cursor.execute(f"UPDATE usercart SET producttotalprice='{newprice}' WHERE rowid='{therowid}'")
    connection.commit()
    connection.close()
    print('Product successfully updated')
    Shopping_Menu()




#Delete Product in Cart
def Delete_Product():
    connection = sqlite3.connect('usercart.db')
    cursor = connection.cursor()
    Print_Cart()
    therowid = input('Enter the row id of the product: ')
    deleteproduct = (f"DELETE from usercart where rowid = {therowid}")
    cursor.execute('''SELECT * FROM usercart''')
    cursor.execute(deleteproduct)
    connection.commit()
    connection.close()
    print('Product successfully deleted in cart')
    Shopping_Menu()



#Proceed to Payment
def Proceed_Payment():
    print('')
    print('='*15,'Payment','='*15)
    print('Are you sure you want to proceed to payment')
    print("1. Go to Payment")
    print("2. Continue Shopping")
   
    option = int(input('\nChoose an option: '))
    while option != 1 and option !=2:
        option = int(input('Choose an option: '))
    
    if option == 1:
        Payment.Start(USERNAME ,PWD)
    elif option == 2:
        Shopping_Menu()

Print_Cart()