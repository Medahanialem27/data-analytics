USE northwind;

-- 1) Find the cheapest price
SELECT MIN(Unitprice) AS cheapest_price
FROM products;

-- 2) Find the average price, rounded to the nearest cent
SELECT ROUND(AVG(UnitPrice), 2) AS average_price
FROM products;

-- 3) Find the highest price, then the product and its supplies
SELECT MAX(UnitPrice) AS highest_price
FROM products;

-- 4) Find total month payroll,
SELECT SUM(Salary) As total_month_payroll
FROM employees;

-- 5) Find the highest and lowest salaries
SELECT MAX(Salary) AS highest_salary,
MIN(Salary) AS lowest_salary
FROM employees;


-- 6) Find each supplie's name, ID, and number of products supplied.
SELECT s.CompanyName AS supplier_name,
s.SupplierID,
COUNT(p.ProductID) AS number_of_items
FROM suppliers AS s
LEFT JOIN products AS p
ON s.SupplierID = p.SupplierID
GROUP BY s.SupplierID, s.CompanyName
ORDER BY s.SupplierID, s.CompanyName;

-- 7) find each categorys name and average product price
SELECT c.CategoryName,
ROUND(AVG(p.Unitprice), 2) AS average_price
FROM Catagories AS c
LEFT JOIN products AS p
ON c.CategoryID = p.CategoryID
GROUP BY c.CategoryID, c.CategoryName;


-- 8) 
SELECT
s.CompanyName AS supplier_name,
COUNT(p.ProductID) AS number_of_items
FROM suppliers AS s
JOIN products AS p
ON s.SupplierID = p.SupplierID
GROUP BY s.SupplierID, s.CompanyName
HAVING COUNT(p.ProductID) >= 5
ORDER BY number_of_items DESC;
-- 9)
SELECT ProductID,
ProductName,
UnitPrice * UnitsInStock AS inventory_value
FROM products
WHERE UnitsInStock > 0
ORDER BY inventory_value DESC, ProductName ASC;







