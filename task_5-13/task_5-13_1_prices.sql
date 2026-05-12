UPDATE prices
SET price = price * 1.1
WHERE price < 1000;

select prices 
from prices
where price < 1000

