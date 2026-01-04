-- Total customers
SELECT COUNT(DISTINCT customer_id) FROM shopping_trends;

-- Category-wise total sales
SELECT category, SUM(`purchase amount (usd)`) AS total_sales
FROM shopping_trends
GROUP BY category
ORDER BY total_sales DESC;

-- Discount impact by category
SELECT category,
COUNT(*) AS total_orders,
SUM(CASE WHEN `discount applied` = 'Yes' THEN 1 ELSE 0 END) AS discount_orders
FROM shopping_trends
GROUP BY category;

-- Age-wise average spending
SELECT age, AVG(`purchase amount (usd)`) AS avg_spend
FROM shopping_trends
GROUP BY age
ORDER BY age;

-- Season-wise sales
SELECT season, SUM(`purchase amount (usd)`) AS season_sales
FROM shopping_trends
GROUP BY season;

-- Payment method usage
SELECT `payment method`, COUNT(*) AS usage_count
FROM shopping_trends
GROUP BY `payment method`;

-- Location-wise spending
SELECT location, AVG(`purchase amount (usd)`) AS avg_spend
FROM shopping_trends
GROUP BY location;
