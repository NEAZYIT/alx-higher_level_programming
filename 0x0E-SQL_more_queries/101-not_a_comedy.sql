-- Task: List shows from the hbtn_0d_tvshows database without the 'Comedy' genre.
-- Retrieve distinct show titles that are not linked to the 'Comedy' genre, sorted by show title in ascending order.
SELECT DISTINCT t.`title`
FROM `tv_shows` AS t
LEFT JOIN `tv_show_genres` AS s ON s.`show_id` = t.`id`
LEFT JOIN `tv_genres` AS g ON g.`id` = s.`genre_id`
WHERE t.`title` NOT IN (
    SELECT `title`
    FROM `tv_shows` AS t
    INNER JOIN `tv_show_genres` AS s ON s.`show_id` = t.`id`
    INNER JOIN `tv_genres` AS g ON g.`id` = s.`genre_id`
    WHERE g.`name` = "Comedy"
)
ORDER BY `title`;
