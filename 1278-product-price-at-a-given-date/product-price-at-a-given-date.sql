# Write your MySQL query statement below
select 
    distinct product_id,
    10 as price
from 
    products
group by
    product_id
having
    min(change_date) > "2019-08-16"

union

select 
    product_id, 
    new_price
from 
    Products 
where 
    (product_id, change_date) in(
                                select 
                                    product_id, 
                                    max(change_date) as recent_date
                                from 
                                    Products
                                where 
                                    change_date <= "2019-08-16"
                                group by 
                                    product_id
                                )