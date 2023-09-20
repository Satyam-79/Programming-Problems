# Write your MySQL query statement below
SELECT
	Activity.player_id  AS player_id,
	min(Activity.event_date) as first_login
FROM
	Activity
GROUP BY
	Activity.player_id