# Write your MySQL query statement below
# SELECT
# 	s.product_id   AS product_id,
# 	p.product_name AS product_name
# FROM
# 	Sales s
# 	INNER JOIN
# 		Product p
# 		ON
# 			s.product_id=p.product_id
# WHERE
# 	s.sale_date BETWEEN '2019-01-01' and '2019-03-31'
#     AND p.product_id NOT IN (SELECT ss.product_id FROM Sales ss 
#           WHERE ss.sale_date NOT BETWEEN '2019-01-01' AND '2019-03-31')

SELECT
	s.product_id   AS product_id,
	p.product_name AS product_name
FROM
	Sales s
	INNER JOIN
		Product p
		ON
			s.product_id=p.product_id
GROUP BY s.product_id 
HAVING 
    MIN(s.sale_date)>='2019-01-01' 
    and MAX(s.sale_date)<='2019-03-31'