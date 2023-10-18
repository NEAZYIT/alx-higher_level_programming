-- Task: List shows in the hbtn_0d_tvshows database without a linked genre.
-- Show titles and NULL genre IDs for shows without genres, ordered by show title and genre ID.
SELECT s.`title`, g.`genre_id`
FROM `tv_shows` AS s
LEFT JOIN `tv_show_genres` AS g
ON s.`id` = g.`show_id`
WHERE g.`genre_id` IS NULL
ORDER BY s.`title`, g.`genre_id`;
