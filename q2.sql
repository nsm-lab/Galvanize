select name 
from salesperson 
where ID in 
(
	select salesperson_id 
	from orders 
	group by salesperson_id 
	having count(*) > 1
);