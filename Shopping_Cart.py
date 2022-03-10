import sqlite3
import sys
import Main

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
    cursor.execute('''SELECT * FROM usercart''')
    result=cursor.fetchall()
    for i in result:
        print(i)
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
    print(f'Welcome {USERNAME}')
    print("1. Add Product into Shopping Cart")
    print("2. Edit Product in Shopping Cart")
    print("3. Delete Product in Shopping Cart")
    print("4. Proceed to Payment")
    print("5. Exit")


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
        Shopping_Menu()



#Add Product for User
def Add_Product():
    Print_Product()
    username = USERNAME
    productid = input('Enter the product id: ')
    productname = input('Enter the product name: ')
    productprice = input('Enter the product price: ')
    productquantity = input('Enter the product quantity: ')
    productproducedby = input('Enter the producer of this product: ')
    productexpirydate = input('Enter the product expiry date: ')
    producttotalprice = input('Enter the product total price: ')
    sellerinformation = input('Enter the seller name: ')
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
    quantitychange = int(input('Enter the new quantity of the product you would like to change: '))
    newprice = input('Enter the new total price:  ')
    editproduct = (f"UPDATE usercart SET productquantity = {quantitychange} where rowid = {therowid}")
    newproductprice = (f"UPDATE usercart SET producttotalprice = {newprice} where rowid = {therowid}")
    cursor.execute(editproduct)
    cursor.execute(newproductprice)
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
    connection = sqlite3.connect('usercart.db')
    cursor = connection.cursor()
    Print_Cart()
    urusername = input('Enter your username for checkout: ')
    proceedpayment = (f"SELECT SUM(producttotalprice) FROM usercart WHERE username = {urusername}")
    cursor.execute(proceedpayment)
    print('The total price for your checkout is')
    print(cursor.fetchone()[0])
    connection.commit()
    connection.close()
    print('Purchases Completed')
    Shopping_Menu()