SELECT
	ROUND((SUM(t.login)/COUNT(DISTINCT t.player_id)),2) AS fraction
FROM
	(
		SELECT
			Activity.player_id,
			DATEDIFF(Activity.event_date,MIN(Activity.event_date) OVER (PARTITION BY Activity.player_id)) =1 AS login
		FROM
			Activity
	)
	AS t