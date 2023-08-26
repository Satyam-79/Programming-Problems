# Write your MySQL query statement below
with cte AS
	(
		SELECT *
		FROM
			Person
	)
DELETE
FROM
	Person
WHERE
	id NOT IN
	(
		SELECT
			MIN(id)
		FROM
			cte
		GROUP BY
			email
	)