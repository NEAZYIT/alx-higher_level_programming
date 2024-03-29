-- Task: List shows in hbtn_0d_tvshows with at least one linked genre.
-- Select show titles and linked genre IDs
SELECT s.`title`, g.`genre_id`
FROM `tv_shows` AS s
INNER JOIN `tv_show_genres` AS g
ON s.`id` = g.`show_id`
ORDER BY s.`title`, g.`genre_id`;
