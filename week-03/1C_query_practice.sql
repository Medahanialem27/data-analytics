USE northwind;

-- 1) products ordered by price, lowest to highest
SELECT ProductID, ProductName, UnitPrice
FROM products
ORDER BY UnitPrice ASC;

-- 2) At least 100 units in stock, highestprice first
SELECT ProductID, ProductName, Unitprice, UnitsInStock
FROM products
WHERE UnitsInStock >= 100
ORDER BY UnitPrice DESC, productName ASC;

-- 3) Same with product name at the tie-breaker
SELECT productID, ProductName, UnitPrice, UnitsInStock
FROM products
WHERE UnitsInStock >= 100
ORDER BY UnitPrice DESC, ProductName ASc;

-- 4) Count distinct customer who placed orders
SELECT COUNT(DISTINCT CustomerID) AS CustomerCount
 FROM orders; 
 
 -- 5) Distint customer by shipping country, largest count first 
 SELECT ShipCountry, COUNT(DISTINCT CustomerID) AS CustomerCount
FROM orders
GROUP BY ShipCountry
ORDER BY CustomerCount DESC;
 
 -- 6) Fewer than 25 in stock and at least one unit on order
SELECT ProductID, ProductName, UnitsInStock, UnitsOnOrder
FROM products
WHERE UnitsInStock < 25
AND UnitsOnOrder >= 1
ORDER BY UnitsOnOrder DESC, ProductName ASC;

-- 7) Employee count by job title
SELECT Title, COUNT(*) AS EmployeeCount
FROM employees
GROUP BY Title;

-- 8) Employees with salary between $2,000 and $2,500
SELECT FirstName, LastName, Title, Salary
FROM employees
WHERE Salary BETWEEN 2000 AND 2500
ORDER BY Title;
 