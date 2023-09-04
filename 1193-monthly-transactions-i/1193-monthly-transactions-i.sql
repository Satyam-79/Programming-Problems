# Write your MySQL query statement below
SELECT
	DATE_FORMAT(tns.trans_date, "%Y-%m") AS month      ,
	tns.country                          AS country    ,
	COUNT(tns.state)                     AS trans_count,
	SUM(
	IF
	(
		tns.state="approved",1,0
	)
	)               AS approved_count    ,
	SUM(tns.amount) AS trans_total_amount,
	SUM(
	IF
	(
		tns.state="approved",tns.amount,0
	)
	) AS approved_total_amount
FROM
	Transactions tns
GROUP BY
	DATE_FORMAT(tns.trans_date, "%Y-%m"),
	tns.country