# Write your MySQL query statement below
SELECT
	Tweets.tweet_id AS tweet_id
FROM
	Tweets
WHERE
	CHAR_LENGTH(Tweets.content)>15