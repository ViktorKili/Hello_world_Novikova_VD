SELECT category, COUNT(*) as product_count
FROM products
GROUP BY category;

SELECT category, COUNT(*) as product_count
FROM products
GROUP BY category
ORDER BY product_count DESC;

