# Write your MySQL query statement below
WITH cte AS
	(SELECT
			Logs.num         AS num  ,
			LEAD(Logs.num,1) OVER() AS num1 ,
			LEAD(Logs.num,2) OVER() AS num2
		FROM
			Logs)
SELECT DISTINCT
	cte.num AS ConsecutiveNums
FROM
	cte
WHERE
	num    =num1
	AND num=num2