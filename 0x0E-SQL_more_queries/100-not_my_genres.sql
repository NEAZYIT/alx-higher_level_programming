-- Task: List genres from the hbtn_0d_tvshows database not linked to the show "Dexter."
-- Retrieve distinct genre names that are not linked to the show "Dexter," sorted by genre name in ascending order.
SELECT DISTINCT g.`name`
FROM `tv_genres` AS g
INNER JOIN `tv_show_genres` AS s ON g.`id` = s.`genre_id`
INNER JOIN `tv_shows` AS t ON s.`show_id` = t.`id`
WHERE g.`name` NOT IN (
    SELECT `name`
    FROM `tv_genres` AS g
    INNER JOIN `tv_show_genres` AS s ON g.`id` = s.`genre_id`
    INNER JOIN `tv_shows` AS t ON s.`show_id` = t.`id`
    WHERE t.`title` = "Dexter"
)
ORDER BY g.`name`;
