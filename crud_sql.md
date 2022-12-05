# CRUD SQL
Below are the SQL statements used to perform CRUD functions for our application.

## Create
The "Create Clothing" tab adds a record to the Product table. All entry fields are required to include Product Type, SupplierID, Size, Material, and Price. The code checks to ensure all entry fields have an input; otherwise, a pop-up window will execute stating to the user that all fields are required. 

The full SQL statement with the TKinter get() function looks like this:

"INSERT INTO Product (Type, SupplierID, Size, Material, Price) VALUES " + '("' + prodTypeEntry.get() + '","' + suppIDEntry.get() + '","' + sizeEntry.get() + '","' + materialEntry.get() + '","' + priceEntry.get() + '")'

An example:
    INSERT INTO Product (Type, SupplierID, Size, Material, Price) VALUES ("Shorts","2","XL","Nylon","14.99")

## Read
The "Read Suppliers Info/Products" tab allows for the reading of two different tables, the Suppliers Table and the Product Table. 

The first entry/button duo "Supplier ID _entry_ BTN: List Products From Supplier" allows a user to input a supplierID and be returned with a list of all product records that are connected to that specific supplierID.
The Full SQL Statement looks like this:
    "SELECT * FROM Product WHERE supplierID=%s" % (supplierIDEntry.get())
An Example:
    SELECT * FROM Product WHERE supplierID=1

The second entry/button duo "Supplier Name _entry_ BTN: List Supplier Info" allows a user to input a supplierName and be returned the supplier Info corresponding to the name to include their address and # of products they have. 
The Full SQL Statement looks like this:
    "SELECT * FROM Suppliers WHERE supplierName=\"%s\"" % (supplierNameEntry.get())
An Example:
    SELECT * FROM Suppliers WHERE supplierName="Watson's Ties"

Both buttons have an error check to ensure an entry is inputted before the button executes the SQL functions. These buttons are independent, and the user can use either button individually.
## Update

The "Update customer info" tab updates one record from the Customers table. CustomerID is a required input to prevent changing all records, but FirstName, LasstName, and Address are all optional. The code will skip over empty entries, meaning that no record will update to empty cells if firstname, lastname, and address are left blank.

When put together, the full SQL statement with the TKinter get() function looks like this

`UPDATE Customers SET FirstName=firstnameEntry.get(), LastName=lastnameEntry.get(), 
Address=addressEntry.get()
WHERE CustomerID = custIDEntry.get()`

Here's an example of what the statement above could look like to MYSQL.

`UPDATE Customers SET FirstName="Jenny", Address="201 N Main St" WHERE CustomerID=5`

## Delete
The "Delete orders" deletes a single order from the Orders table, given the OrderID from input. OrderID is a required input.

`DELETE FROM Orders WHERE OrderID=orderIDEntry.get()`

Here's an example of what the statement above could look like to MYSQL.

`DELETE FROM Orders WHERE OrderID=5`

## Predefined SQL Buttons

The button "Show Customer Info by OrderID" does an INNER JOIN between the Orders and Customers tables to be able to grab customer info and connect it with their specific order ID.

The SQL Statement:
    "SELECT Orders.OrderID, Customers.lastname, Customers.address FROM Orders INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID"
An example of the fetched results:
    [(3, 'Smith', '200 Something Ave')]

The button "Show Product Info by SupplierID" does an INNER JOIN between the Product and Suppliers tables to be able to show the productID's and Types of Products associated with each SupplierID.

The SQL Statement:
    SELECT Suppliers.SupplierID, Product.ProductID, Product.Type FROM Suppliers INNER JOIN Product ON Suppliers.SupplierID = Product.SupplierID
An example of the fetched results:
    [(1, 9, 'T-Shirt')]
