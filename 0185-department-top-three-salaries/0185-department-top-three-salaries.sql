# Write your MySQL query statement below
WITH tbl AS
	(
		SELECT
			Department.name AS Department,
			Employee.name   AS Employee  ,
			Employee.salary as Salary    ,
			DENSE_RANK() OVER (PARTITION BY Department.id ORDER BY
							   Employee.salary DESC) AS 'rank'
		FROM
			Employee
			JOIN
				Department
				ON
					Employee.departmentId = Department.id
	)
SELECT
	t.Department,
	t.Employee  ,
	t.Salary
FROM
	tbl t
WHERE
	t.rank<=3