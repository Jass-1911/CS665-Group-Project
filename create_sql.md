## MySQL statements to create the 4 tables 

## Suppliers
CREATE TABLE Suppliers (SupplierID int NOT NULL PRIMARY KEY AUTO_INCREMENT, supplierName VARCHAR(50) NOT NULL, address VARCHAR(50), numOfProducts int)")

## Product
CREATE TABLE Product (ProductID int NOT NULL PRIMARY KEY AUTO_INCREMENT, Type VARCHAR(50), SupplierID int NOT NULL, FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID), Size ENUM('S', 'M', 'L'), Material VARCHAR(50), Price double NOT NULL)")

## Customers
CREATE TABLE Customers(CustomerID int NOT NULL PRIMARY KEY AUTO_INCREMENT, firstName VARCHAR(50) NOT NULL, lastName VARCHAR(50) NOT NULL, address VARCHAR(50))")

## Orders
CREATE TABLE Orders(OrderID int NOT NULL PRIMARY KEY AUTO_INCREMENT, ProductID int, FOREIGN KEY (ProductID) REFERENCES Product(ProductID), CustomerID int, FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID), Total int NOT NULL)")
