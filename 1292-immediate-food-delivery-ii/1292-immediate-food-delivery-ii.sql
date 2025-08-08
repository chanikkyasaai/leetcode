# Write your MySQL query statement below
select
round((select count(*) from ((select customer_id, min(order_date) as firstorder from Delivery group by customer_id ) d1 join Delivery d2 on d1.customer_id = d2.customer_id) where d1.firstorder = d2.customer_pref_delivery_date) *100/ (select count(distinct(customer_id)) from Delivery),2)
as immediate_percentage 