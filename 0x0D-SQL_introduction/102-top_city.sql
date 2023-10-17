-- Display the top 3 cities' average temperatures during July and August, ordered by temperature in descending order
SELECT city, AVG(value) AS avg_temp
FROM `temperatures`
WHERE MONTH(date) IN (7, 8)
GROUP BY `city`
ORDER BY AVG(value) DESC
LIMIT 3;
