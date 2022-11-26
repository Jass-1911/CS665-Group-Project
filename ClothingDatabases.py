import mysql
import mysql.connector
import tkinter

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="", #insert whatever password was made when installing MySQL
    database="testdb"
)

dbCursor = db.cursor()

#dbCursor.execute("DROP TABLE Suppliers")

#--Creating table operations
# dbCursor.execute("CREATE TABLE Suppliers (SupplierID int NOT NULL PRIMARY KEY AUTO_INCREMENT, supplierName VARCHAR(50) NOT NULL, address VARCHAR(250), numOfProducts int)")
# dbCursor.execute("CREATE TABLE Product (ProductID int NOT NULL PRIMARY KEY AUTO_INCREMENT, Type VARCHAR(10), SupplierID int NOT NULL, FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID), Size ENUM('XS', 'S', 'M', 'L', 'XL'), Material VARCHAR(10), Price double NOT NULL)")
# dbCursor.execute("CREATE TABLE Customers(CustomerID int NOT NULL PRIMARY KEY AUTO_INCREMENT, firstName VARCHAR(50) NOT NULL, lastName VARCHAR(50) NOT NULL, address VARCHAR(250))")
# dbCursor.execute("CREATE TABLE Orders(OrderID int NOT NULL PRIMARY KEY AUTO_INCREMENT, ProductID int, FOREIGN KEY (ProductID) REFERENCES Product(ProductID), CustomerID int, FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID), Total double NOT NULL)")

# -- Alters tables for starting IDs that will increment by 1
# dbCursor.execute("ALTER TABLE Suppliers AUTO_INCREMENT=100")
# dbCursor.execute("ALTER TABLE Customers AUTO_INCREMENT=200")
# dbCursor.execute("ALTER TABLE Orders AUTO_INCREMENT=300")

#--Drop/Delete table operations:
# dbCursor.execute("DROP TABLE Orders")
# dbCursor.execute("DROP TABLE Customers")
# dbCursor.execute("DROP TABLE Product")
# dbCursor.execute("DROP TABLE Suppliers")


#--Insert into table operations
#--SUPPLIERS--
# dbCursor.execute("INSERT INTO Suppliers (supplierName, address, numOfProducts) VALUES (%s,%s,%s)", ("Watson's Ties", "500 Baker ST", 1)) #id=100
# dbCursor.execute("INSERT INTO Suppliers (supplierName, address, numOfProducts) VALUES (%s,%s,%s)", ("Shopper's Wholesale", "1234 Blue Ave", 1)) #id = 113
# dbCursor.execute("INSERT INTO Suppliers (supplierName, address, numOfProducts) VALUES (%s,%s,%s)", ("Shoes In Bulk", "5120 Sneaker ST", 1)) #id = 114
# dbCursor.execute("INSERT INTO Suppliers (supplierName, address, numOfProducts) VALUES (%s,%s,%s)", ("Dresses For Success", "777 Lucky Blvd", 1)) # id = 115
# dbCursor.execute("INSERT INTO Suppliers (supplierName, address, numOfProducts) VALUES (%s,%s,%s)", ("The Shirt Depot", "987 34th ST", 1)) # id = 116

# #--PRODUCTS--
# dbCursor.execute("INSERT INTO Product (Type, SupplierID, Size, Material, Price) VALUES (%s,%s,%s,%s,%s)", ("Tie", 100, 'M', "Silk", 20.00))
# dbCursor.execute("INSERT INTO Product (Type, SupplierID, Size, Material, Price) VALUES (%s,%s,%s,%s,%s)", ("Shirt", 104, 'L', "Cotton", 45.00))
# dbCursor.execute("INSERT INTO Product (Type, SupplierID, Size, Material, Price) VALUES (%s,%s,%s,%s,%s)", ("Dress", 103, 'S', "Velvet", 60.00))
# dbCursor.execute("INSERT INTO Product (Type, SupplierID, Size, Material, Price) VALUES (%s,%s,%s,%s,%s)", ("Shoes", 102, 'XS', "Canvas", 50.00))
# dbCursor.execute("INSERT INTO Product (Type, SupplierID, Size, Material, Price) VALUES (%s,%s,%s,%s,%s)", ("Pants", 101, 'XL', "Polyester", 39.00))


#--CUSTOMERS--
# dbCursor.execute("INSERT INTO Customers (firstName, lastName, address) VALUES (%s,%s,%s)", ("Nathan", "Smith", "200 Something Ave"))
# dbCursor.execute("INSERT INTO Customers (firstName, lastName, address) VALUES (%s,%s,%s)", ("Aaron", "Will", "2560 Red ST"))
# dbCursor.execute("INSERT INTO Customers (firstName, lastName, address) VALUES (%s,%s,%s)", ("Tina", "Young", "6802 Orange Blvd"))
# dbCursor.execute("INSERT INTO Customers (firstName, lastName, address) VALUES (%s,%s,%s)", ("Winona", "Borowski", "3331 23rd ST"))
# dbCursor.execute("INSERT INTO Customers (firstName, lastName, address) VALUES (%s,%s,%s)", ("Paul", "Walker", "2305 Access Ave"))

#--ORDERS--
# dbCursor.execute("INSERT INTO Orders (ProductID, CustomerID, Total) VALUES (%s,%s,%s)", (1, 200, 20.00))
# dbCursor.execute("INSERT INTO Orders (ProductID, CustomerID, Total) VALUES (%s,%s,%s)", (2, 204, 45.00))
# dbCursor.execute("INSERT INTO Orders (ProductID, CustomerID, Total) VALUES (%s,%s,%s)", (4, 202, 50.00))
# dbCursor.execute("INSERT INTO Orders (ProductID, CustomerID, Total) VALUES (%s,%s,%s)", (3, 203, 60.00))
# dbCursor.execute("INSERT INTO Orders (ProductID, CustomerID, Total) VALUES (%s,%s,%s)", (5, 201, 39.00))





#----EXPLORTING OPERATIONS
#Deleting

# --Orders
# val = input("Enter OrderID you wish to delete: ")
# inputString = "DELETE FROM Orders WHERE OrderID="+val
# dbCursor.execute(inputString) #delete an entry

#--Customers -- will not delete if an row in Orders exists with CustomerID
# val = input("Enter CustomerID you wish to delete: ")
# inputString = "DELETE FROM Customers WHERE CustomerID="+val
# dbCursor.execute(inputString) #delete an entry

#--Products -- will not delete if row in Orders exists with OrderID
# val = input("Enter ProductID you wish to delete: ")
# inputString = "DELETE FROM Product WHERE ProductID="+val
# dbCursor.execute(inputString) #delete an entry

#--Suppliers -- will not delete if a row in Products exists with SupplierID
# val = input("Enter SupplierID you wish to delete: ")
# inputString = "DELETE FROM Suppliers WHERE SupplierID="+val
# dbCursor.execute(inputString) #delete an entry


#Updating

#--Customers
# first_name = input("Enter first name: ")
# last_name = input("Enter last name: ")
# up_address = input("Enter address: ")
# updateString = "UPDATE Customers SET firstName='"+first_name+"', lastName='"+last_name+"', address='"+up_address+"' WHERE CustomerID=200"
# dbCursor.execute(updateString)
#dbCursor.execute("UPDATE Customers SET firstName='Ralph', lastName='Smith', address='230 Something Ave' WHERE CustomerID=200")

#--Orders
# product_id = input("Enter ProductID for order: ")
# customer_id = input("Enter CustomerID for order: ")
# total_entry = input("Enter total for order: ")
# updateString2 = "UPDATE Orders SET ProductID="+product_id+", CustomerID="+customer_id+", Total="+total_entry+" WHERE OrderID=302"
# dbCursor.execute(updateString2)

#--Product
# type = input("Enter type for product: ")
# supplier_id = input("Enter supplier ID for product: ")
# size = input("Enter size of product: ")
# material = input("Enter material of product: ")
# price = input("Enter price for product: ")
# updateString3 = "UPDATE Product SET Type='"+type+"', SupplierID="+supplier_id+", Size='"+size+"', Material='"+material+"', Price="+price+" WHERE ProductID=4"
# dbCursor.execute(updateString3)


#--Suppliers
# supplier_name = input("Enter name for supplier: ")
# address = input("Enter address of supplier: ")
# num_products = input("Enter number of products from supplier: ")
# updateString3 = "UPDATE Suppliers SET supplierName='"+supplier_name+"', address='"+address+"', numOfProducts="+num_products+" WHERE SupplierID=103"
# dbCursor.execute(updateString3)

#Creating

#--Suppliers
# supplier_name = input("Enter name for supplier: ")
# address = input("Enter address of supplier: ")
# num_products = input("Enter number of products from supplier: ")
# createString1 = "INSERT INTO Suppliers (supplierName, address, numOfProducts) VALUES (%s,%s,%s)"
# dbCursor.execute(createString1,(supplier_name, address, num_products))

#--Product
# type = input("Enter type for product: ")
# supplier_id = input("Enter supplier ID for product: ")
# size = input("Enter size of product: ")
# material = input("Enter material of product: ")
# price = input("Enter price for product: ")
# createString2 = "INSERT INTO Product (Type, SupplierID, Size, Material, Price) VALUES (%s,%s,%s,%s,%s)"
# dbCursor.execute(createString2, (type, supplier_id, size, material, price))

#--Orders
# product_id = input("Enter ProductID for order: ")
# customer_id = input("Enter CustomerID for order: ")
# total_entry = input("Enter total for order: ")
# createString3 = "INSERT INTO Orders (ProductID, CustomerID, Total) VALUES (%s,%s,%s)"
# dbCursor.execute(createString3, (product_id, customer_id, total_entry))

#--Customers
# first_name = input("Enter first name: ")
# last_name = input("Enter last name: ")
# up_address = input("Enter address: ")
# createString4 = "INSERT INTO Customers (firstName, lastName, address) VALUES (%s,%s,%s)"
# dbCursor.execute(createString4, (first_name, last_name, up_address))



db.commit()


#def readTable():
 #   print("Read")
 #  dbCursor.execute("SELECT * FROM Product")


# def updateTable():
#     print("Updated")
#     # dbCursor.execute("UPDATE TABLE SET * WHERE *")


# def deleteRel():
#     print("Deleted")
#     # dbCursor.execute("DELETE FROM TABLE Customers WHERE CustomerID=200")


#--------READS TABLES
dbCursor.execute("SELECT * FROM Suppliers")
for x in dbCursor:
    print(x)
dbCursor.execute("SELECT * FROM Product")
for x in dbCursor:
    print(x)
dbCursor.execute("SELECT * FROM Customers")
for x in dbCursor:
    print(x)
dbCursor.execute("SELECT * FROM Orders")
for x in dbCursor:
    print(x)

#------DESCRIBES TABLES
# dbCursor.execute("DESCRIBE Customers")
# for x in dbCursor:
#         print(x)

# dbCursor.execute("DESCRIBE Orders")
# for x in dbCursor:
#         print(x)

#mycursor.execute("CREATE DATABASE testdb")

#CREATE TABLE Scores (userId int PRIMARY KEY, FOREIGN KEY(userID) REFERENCES Users(id), game1 int, )
# Q3 ="INSERT INTO Users(name,passwrd) VALUES (%s, %s)"
#

#top = tkinter.Tk()
# Code to add widgets will go here...
#top.mainloop()



#print(mydb)
#CREATE DATABASE testDB
#CREATE TABLE table_name (
    #PersonID int
#)
