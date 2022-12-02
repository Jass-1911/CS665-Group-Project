## Description of Clothing Database

## Tables
Product(ProductID, Type, SupplierID, Size, Material, Price)
Customers(CustomerID, firstName, lastname, address)
Orders(OrderID, ProductID, CustomerID, Total)
Suppliers(SupplierID, supplierName, address, numOfProducts)

Products represents all the products available in the online clothing store
    - ProductID is the unique ID for each product
    - Type is the type of clothing a product is: dress, tie, shoes, shirt, etc.
    - SupplierID is the int ID of the supplier the product is from
    - Size is ENUM attribute that can be XS, S, M, L, or XL
    - Material is what the product is made of (Silk, cotton, polyester, etc)
    - Price is how much the item costs in USD

Customers represents all the customers of the clothing store
    - CustomerID is the unique ID for each customer (in case several customers have the same name)
    - firstName stores a customer's first name
    - lastName stores a customer's last name
    - address stores a customer's address

Orders represents all the orders made by customers of the clothing store
    - OrderID is the unique ID for each order
    - ProductID is the ID of the product ordered
    - CustomerID is ID of the customer who made the order
    - Total is the total cost of the order (not dependent on the product cost alone, appropriate shipping and tax expenses would be included in the total)

Suppliers represents all the suppliers that the clothing store gets their products from
    - SupplierID is the unique ID for each supplier (in case suppliers have same names)
    - supplierName is the name of the supplier
    - address is the address of the supplier
    - numOfProducts is the int amount of products the supplier has (not dependent on the product table)


## Primary Keys
ProductID
CustomerID
OrderID
SupplierID

## Foreign Keys and Constraints
SupplierID 
    - is a FK in the Product table, references the parent table of Product -> Suppliers(SupplierID)
CustomerID
    - is a FK in the Orders table, references the parent table of Orders -> Customers(CustomerID)
ProductID
    - is a FK in the Orders table, references the parent table of Orders -> Product(ProductID)


## Functional Dependencies
Product:
    ProductID -> Type, SupplierID, Size, Material, Price

Customers:
    CustomerID -> FirstName, Lastname, Address

Orders:
    OrderID -> ProductID, CustomerID, Total

Suppliers:
    SupplierID -> supplierName, address, numOfProducts


## 3NF?
All tables are in 3NF, no transitive dependencies for non-prime attributes

## Sample Rows
Product:
    INSERT INTO Product
    VALUES (1, "Tie", 100, 'M', "Silk", 20.00)

Suppliers:
    INSERT INTO Suppliers
    VALUES (100, "Watson's Ties", "500 Baker ST", 1)

Customers:
    INSERT INTO Customers
    VALUES (200, "Nathan", "Smith", "200 Something Ave")

Orders:
    INSERT INTO Orders
    VALUES (300, 1, 200, 20.00)










