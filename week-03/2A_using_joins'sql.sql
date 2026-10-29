USE northwind;
-- 1) List products with their category names
SELECT p.productID, p.productname, p.unitprice, c.categoryname
FROM products AS p
JOIN categories AS c
ON p.categoryID = c.CategoryID;
ORDER BY c.categoryname, p.productname;

-- 2) Products over $75 with supplier names
SELECT p.productID, p.productname, p.unitprice, s.CompanyName AS suppliername
FROM products AS p
JOIN suppliers AS s ON p.supplierID = s.supplierID
WHERE  p.unitprice > 75
ORDER BY p.productname;

-- 3) List every product with category 
SELECT p.productID, p.productname, p.unitprice, c.categoryname, s.CompanyName AS suppliername
FROM products AS p
JOIN categories AS c 
ON p.categoryID = c.categoryID
 JOIN suppliers AS s 
ON p.supplierID = s.supplierID
ORDER BY p.productname;

-- 4) Order shipn to Germany
SELECT o.OrderID, o.ShipName, o.ShipAddress,
s.CompanyName AS Shipper
FROM orders AS o
JOIN shippers AS s
ON o.ShipVia = s.ShipperID
WHERE o.ShipCountry = 'Germany'
ORDER BY Shipper, o.ShipName;

-- 5) Count Germany orders
SELECT s.CompanyName AS Shipper, COUNT(o.OrderID) AS Ordercount
FROM orders AS o
JOIN shippers AS s
ON o.ShipVia = s.ShipperID
WHERE o.ShipCountry = 'Germany'
GROUP BY s.CompanyName
ORDER BY s.CompanyName;

-- 6 Orders that inculded surround
SELECT DISTINCT o.OrderID, o.OrderDate, o.ShipName, o.ShipAddress
FROM orders AS o
JOIN `order details` AS od
ON o.OrderID = od.OrderID
JOIN products AS p
ON od.ProductID = p.ProductID
WHERE p.ProductName = 'Sasquatch Ale';
