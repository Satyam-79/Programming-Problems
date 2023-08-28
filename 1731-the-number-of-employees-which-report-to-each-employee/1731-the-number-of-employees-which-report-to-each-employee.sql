# Write your MySQL query statement below
SELECT
	e.employee_id        AS employee_id  ,
	e.name               AS name         ,
	COUNT(e.employee_id) AS reports_count,
	ROUND(AVG(m.age))    AS average_age
# FROM
# 	Employees e,
# 	Employees m
# WHERE
# 	e.employee_id=m.reports_to
FROM
	Employees e
	INNER JOIN
		Employees m
		ON
			e.employee_id=m.reports_to
GROUP BY employee_id
ORDER BY employee_id