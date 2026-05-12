SELECT product_id, COUNT(*) as suppliers_count
FROM suppliers
GROUP BY product_id;

