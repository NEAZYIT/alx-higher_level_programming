-- Task: List comedy shows in the hbtn_0d_tvshows database.
-- Retrieve show titles categorized as "Comedy," sorted by show title in descending order.
SELECT t.`title`
FROM `tv_shows` AS t
INNER JOIN `tv_show_genres` AS s ON t.`id` = s.`show_id`
INNER JOIN `tv_genres` AS g ON g.`id` = s.`genre_id`
WHERE g.`name` = "Comedy"
ORDER BY t.`title` DESC;
