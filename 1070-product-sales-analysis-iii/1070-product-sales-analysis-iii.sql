# Write your MySQL query statement below

# WITH first_year_sales AS (
#     SELECT 
#         s.product_id,
#         MIN(s.year) AS first_year
#     FROM 
#         Sales s
#     INNER JOIN 
#         Product p ON p.product_id = s.product_id
#     GROUP BY 
#         s.product_id
# )

# SELECT 
#     f.product_id,
#     f.first_year,
#     s.quantity,
#     s.price
# FROM 
#     first_year_sales f
# JOIN 
#     Sales s ON f.product_id = s.product_id AND f.first_year = s.year

select product_id, year as first_year, quantity, price
from
(
select *, rank() over(partition by product_id order by year) as year_rnk
from sales
) as tbl
where year_rnk = 1