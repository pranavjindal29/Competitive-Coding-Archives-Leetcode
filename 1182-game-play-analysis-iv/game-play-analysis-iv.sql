WITH first_logins AS (
    SELECT player_id, MIN(event_date) AS first_date
    FROM Activity
    GROUP BY player_id
)
SELECT ROUND(
    COUNT(DISTINCT a2.player_id) / 
    COUNT(DISTINCT f.player_id), 
    2
) AS fraction
FROM first_logins f
LEFT JOIN Activity a2
    ON a2.player_id = f.player_id
    AND a2.event_date = DATE_ADD(f.first_date, INTERVAL 1 DAY);