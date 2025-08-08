# Write your MySQL query statement below
select 
s.user_id, 
round(coalesce(c.conf/t.total,0),2)  as confirmation_rate from Signups s left join
(select user_id, count(user_id) as total from Confirmations group by user_id) t 
on s.user_id = t.user_id
left join 
(select user_id, count(user_id) as conf from Confirmations where action = 'confirmed' group by user_id) c
on t.user_id = c.user_id