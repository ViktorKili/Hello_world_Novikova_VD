SELECT p.name, pr.price
FROM products AS p
JOIN prices AS pr ON p.id = pr.product_id;