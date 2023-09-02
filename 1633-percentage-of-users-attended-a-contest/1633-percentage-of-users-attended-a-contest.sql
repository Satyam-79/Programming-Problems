# Write your MySQL query statement below
SELECT
	Register.contest_id,
	ROUND(count(Register.contest_id)*100/
	(
		SELECT
			COUNT(Users.user_id)
		FROM
			Users
	)
	,2 ) AS percentage
FROM
	Register
GROUP BY
	Register.contest_id
ORDER BY
	percentage DESC,
	Register.contest_id ASC