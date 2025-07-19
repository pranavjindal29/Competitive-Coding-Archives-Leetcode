SELECT 
    c1.visited_on, 
    SUM(amount) AS amount, 
    ROUND(SUM(amount) / 7, 2) AS average_amount
FROM 
    (
        SELECT DISTINCT visited_on 
        FROM Customer 
        GROUP BY visited_on
    ) AS c1, 
    Customer c2
WHERE 
    c2.visited_on BETWEEN DATE_SUB(c1.visited_on, INTERVAL 6 DAY) AND c1.visited_on
GROUP BY 
    c1.visited_on
HAVING 
    COUNT(DISTINCT c2.visited_on) >= 7
ORDER BY 
    c1.visited_on;