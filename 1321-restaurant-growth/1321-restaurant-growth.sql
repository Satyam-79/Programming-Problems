# Write your MySQL query statement below
WITH cte AS
	(
		SELECT
			visited_on,
			SUM(c.amount) AS amount
		FROM
			Customer c
		GROUP BY
			c.visited_on
	)
SELECT
	t1.visited_on AS visited_on,
	SUM(t2.amount )    AS amount    ,
	ROUND(SUM(t2.amount)/7,2) AS average_amount 
FROM
	cte t1
	JOIN
		cte t2
		ON
			DATEDIFF(t1.visited_on,t2.visited_on) BETWEEN 0 AND 6
GROUP BY
	t1.visited_on
HAVING DATEDIFF(t1.visited_on, (SELECT min(visited_on) from Customer))>=6
ORDER BY
	t1.visited_on