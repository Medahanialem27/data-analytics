USE northwind;

-- 1) what is the product name the must expensive products?
SELECT ProductName
FROM products
WHERE Unitprice = (
SELECT MAX(UnitPrice)
FROM products
);

-- 2) what is the product name and categry of the least expensive products
SELECT p.ProductName, c.CategoryName
FROM products AS p
JOIN categories AS c
ON p.categoryID = c.CategoryID
WHERE p.UnitPrice = (
SELECT MIN(UnitPrice)
FROM products
);

-- 3) what is the order id shipping name and shipping address
SELECT OrderID, ShipName, ShipAddress
FROM orders
WHERE ShipVia IN (
    SELECT ShipperID
    FROM shippers
    WHERE CompanyName = 'Federal Shipping'
    );
    
    -- 4) what are the order id that inciuded sasquatch Ale
    SELECT DISTINCT orderID
    FROM `order details`
    WHERE productID IN (
    SELECT productID
    FROM products
    WHERE productname = 'Sasquatch Ale'
    );
-- 5) What is the name of employee that sold order 10266
SELECT FirstName, LastName
FROM employees
WHERE EmployeeID = (
SELECT EmployeeID
FROM orders
WHERE OrderID = 10266
);

-- 6) What is the name of the customer that bought order 10266?
SELECT CompanyName
FROM Customers
WHERE CustomerID =(
SELECT CustomerID
From orders
WHERE OrderID = 10266
);








