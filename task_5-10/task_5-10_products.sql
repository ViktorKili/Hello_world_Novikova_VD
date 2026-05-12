--First
select *
from products;

--Second
select name, category
from products;

--Third
SELECT distinct category
from products;

--Forth
select *
from products
order by name asc;

--Fifth
select *
from products
order by name desc;

--Sixth
SELECT * 
FROM products
LIMIT 10;

--Seventh
SELECT * 
FROM products
LIMIT 10 OFFSET 10;

--Eights
SELECT * 
FROM products
ORDER BY RANDOM()
LIMIT 5;

--Nineth
SELECT category 
FROM products
GROUP BY category
ORDER BY category ASC;

--Tenth
SELECT * 
FROM products
ORDER BY category, name;

