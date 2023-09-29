# Write your MySQL query statement below
SELECT
	ROW_NUMBER() OVER (ORDER BY
	CASE
		WHEN id%2=0
			THEN id-1
			ELSE id+1
	END) AS id,
	Student
FROM
	Seat
ORDER BY
	id