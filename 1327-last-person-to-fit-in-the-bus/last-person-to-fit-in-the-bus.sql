SELECT person_name from (SELECT person_name,turn,
sum(weight) over (order by turn) AS cum FROM queue) p1
where cum<=1000 order by turn DESC limit 1;