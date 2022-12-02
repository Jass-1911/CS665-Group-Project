## MySQL statements to insert content into the 4 tables 

## Suppliers
INSERT INTO Suppliers
VALUES
  (100, "Watson's Ties", "500 Baker ST", 1),
  (113, "Shopper's Wholesale", "1234 Blue Ave", 1),
  (114, "Shoes In Bulk", "5120 Sneaker ST", 1),
  (115, "Dresses For Success", "777 Lucky Blvd", 1)
  (116, "The Shirt Depot", "987 34th ST", 1);

## Product
INSERT INTO Product
VALUES
  (1, "Tie", 100, 'M', "Silk", 20.00),
  (2, "Shirt", 104, 'L', "Cotton", 45.00)
  (3, "Dress", 103, 'S', "Velvet", 60.00)
  (4, "Shoes", 102, 'XS', "Canvas", 50.00)
  (5, "Pants", 101, 'XL', "Polyester", 39.00);

## Customers
INSERT INTO Customers
VALUES
  (200, "Nathan", "Smith", "200 Something Ave"),
  (201, "Aaron", "Will", "2560 Red ST"),
  (202, "Tina", "Young", "6802 Orange Blvd"),
  (203, "Winona", "Borowski", "3331 23rd ST"),
  (204, "Paul", "Walker", "2305 Access Ave");

## Orders
INSERT INTO Orders
VALUES
  (300, 1, 200, 20.00),
  (301, 2, 204, 45.00),
  (302, 4, 202, 50.00),
  (303, 3, 203, 60.00),
  (304, 5, 201, 39.00);
