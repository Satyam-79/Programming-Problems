# Write your MySQL query statement below

# SELECT
# 	e.name AS Employee
# FROM
# 	Employee e
# 	INNER JOIN
# 		Employee m
# 		ON
# 			e.managerId=m.id
# WHERE
# 	m.salary<e.salary
# ;

select
	b.name as Employee
from
	employee a,
	employee b
where
	a.id = b.ManagerId
	and a.salary < b.salary
	