# CRUD SQL
Below are the SQL statements used to perform CRUD functions for our application.

## Create

## Read

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
