# Write your MySQL query statement below
SELECT
	Followers.user_id AS user_id,
	COUNT(Followers.follower_id) AS followers_count
FROM
	Followers
GROUP BY
	Followers.user_id
ORDER BY
    Followers.user_id ASC