## MySQL statements to create the 4 tables 

## Suppliers
CREATE TABLE Suppliers (
    SupplierID int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    supplierName VARCHAR(50) NOT NULL,
    address VARCHAR(250),
    numOfProducts int)

## Product
CREATE TABLE Product (
    ProductID int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    Type VARCHAR(10),
    SupplierID int NOT NULL,
    FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID),
    Size ENUM('XS', 'S', 'M', 'L', 'XL'),
    Material VARCHAR(10),
    Price double NOT NULL)

## Customers
CREATE TABLE Customers(
    CustomerID int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    firstName VARCHAR(50) NOT NULL,
    lastName VARCHAR(50) NOT NULL,
    address VARCHAR(250))

## Orders
CREATE TABLE Orders(
    OrderID int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    ProductID int,
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID),
    CustomerID int, 
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    Total double NOT NULL)

## Altering IDS in Suppliers, Customers, and Orders to start incrementing at specific value
ALTER TABLE Suppliers AUTO_INCREMENT=100
ALTER TABLE Customers AUTO_INCREMENT=200
ALTER TABLE Orders AUTO_INCREMENT=300
