# Write your MySQL query statement below
select product_id, new_price as price from Products where (product_id, change_date) in (SELECT    
    distinct product_id,
    MAX(change_date) OVER(PARTITION BY product_id) AS m_date
FROM
    Products
where
    change_date<="2019-08-16"
	)
union 
SELECT product_id, 10 AS price
FROM Products
GROUP BY product_id
HAVING MIN(change_date) > '2019-08-16'