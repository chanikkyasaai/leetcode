# Write your MySQL query statement below
select
round(
    (select count(*) from (select player_id, min(event_date) as sd from Activity group by player_id) s
     join Activity a on s.player_id = a.player_id
     where datediff(a.event_date, s.sd) = 1 )
    /(select count(distinct(player_id)) from Activity),2) as fraction