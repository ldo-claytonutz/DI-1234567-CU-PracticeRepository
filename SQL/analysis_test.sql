USE [zzz_ldo]; 
GO

--Request: Return all order details for orders handled by employee #5 where any individual product line in those orders has a quantity greater than 20 units.

WITH orderID_Lookup AS (
    SELECT * 
    FROM [dbo].[orders]
    WHERE EmployeeID = 5
)
SELECT * 
FROM [dbo].[order_details] a
where a.OrderID in (select DISTINCT OrderID from orderID_Lookup)
and Quantity > 20
ORDER BY Quantity DESC; 
