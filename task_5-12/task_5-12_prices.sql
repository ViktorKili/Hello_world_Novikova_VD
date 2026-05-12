SELECT product_id, COUNT(*) as prices_count
FROM prices
GROUP BY product_id;

SELECT product_id, AVG(price) as average_price
FROM prices
GROUP BY product_id;

SELECT product_id, MIN(price) as min_price
FROM prices
GROUP BY product_id;

SELECT product_id, MAX(price) as max_price
FROM prices
GROUP BY product_id;