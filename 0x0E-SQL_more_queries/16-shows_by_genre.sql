-- Task: List shows and linked genres from the hbtn_0d_tvshows database.
-- Retrieve show titles and linked genre names, ordered by show title and genre name in ascending order.
SELECT t.`title`, g.`name`
FROM `tv_shows` AS t
LEFT JOIN `tv_show_genres` AS s ON t.`id` = s.`show_id`
LEFT JOIN `tv_genres` AS g ON s.`genre_id` = g.`id`
ORDER BY t.`title`, g.`name`;
