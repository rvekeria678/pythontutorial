-- Leetcode Problem #607: Sales Person

SELECT name
FROM SalesPerson
LEFT JOIN Orders
ON Orders.sales_id = SalesPerson.sales_id
WHERE SalesPerson.sales_id NOT IN (SELECT sales_id FROM Orders WHERE com_id = 1)
