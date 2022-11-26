# CRUD SQL
Below are the SQL statements used to perform CRUD functions for our application.

## Create

## Read

## Update

The "Update customer info" tab updates one record from the Customers table.
The function required the customerID from input to prevent changing all records, but made firstname, lastname, and address inputs optional. 

When put together, the full SQL statement looks something like this

`UPDATE Customers SET FirstName = "firstnameEntry.get()", LastName = "lastnameEntry.get()", 
Address = "addressEntry.get()"
WHERE CustomerID = custIDEntry.get()`

## Delete
The "Delete orders" deletes a single order from the Orders table, given the OrderID from input.

`DELETE FROM Orders WHERE OrderID=orderIDEntry.get()`
