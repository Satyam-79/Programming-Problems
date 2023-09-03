# Write your MySQL query statement below
SELECT
	Queries.query_name                                    as query_name,
	ROUND(AVG(Queries.rating / Queries.position),2)                AS quality   ,
	ROUND(AVG(IF (Queries.rating < 3, 1, 0)) * 100,2) AS poor_query_percentage
FROM
	Queries
GROUP BY
	query_name