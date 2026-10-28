USE northwind;
SELECT * FROM products;

SELECT * FROM employees;

-- Margaret Peacock is the employee whose name sounds like a bird.
SELECT * FROM categories;
-- Seafood category ID is 8.
SELECT OrderID, OrderDate, ShipName, ShipCountry
FROM orders
LIMIT 50;
SELECT * FROM products;
SELECT * FROM products LIMIT 10;
-- Limet 10 return at most 10 rows.

SELECT OrderID, OrderDate, ShipName, ShipCountry
FROM orders
LIMIT 50;
