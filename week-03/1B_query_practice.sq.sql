USE northwind;
 -- 1. Product ID, name, and price
SELECT ProductID, ProductName, UnitPrice
FROM products;
-- 2. products priced at $7.50 or less
SELECT ProductID, productName, UnitPrice
FROM products 
WHERE UnitPrice <= 7.50;
-- 3 No stock on, on hand, but at last one unit on order
SELECT ProductID, productName, UnitsInstock, UnitsOnOrder
FROM Products
WHERE UnitsInStock = 0 
AND UnitsOnOrder >= 1;

-- 4 Inspect product categories, then list Seafood products
SELECT * FROM Products;
SELECT * FROM Categories;

SELECT ProductID, ProductName, CategoryID
FROM products
WHERE CategoryID = 8;

-- 5 Find Tokyo Traders supplier ID, then its produts
SELECT SupplierID, CompanyName
FROM Suppliers
WHERE CompanyName = 'Tokyo Traders';

-- 6 Count employees, then find titles containing "manager"
SELECT COUNT(*) AS EmployeeCount
FROM employees;

SELECT FirstName, LastName, Title
FROM employees
WHERE Title LIKE '%manager%';



