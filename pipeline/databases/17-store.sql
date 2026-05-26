-- Counts 
SELECT items.name , (items.quantity - IFNULL(sum(orders.number), 0)) AS quantity
FROM items
LEFT JOIN orders ON orders.item_name = items.name
GROUP BY items.name, items.quantity;