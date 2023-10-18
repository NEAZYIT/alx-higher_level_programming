-- Task: List TV shows with at least one linked genre
-- Task: List TV shows with at least one linked genre

-- Select TV show titles and their linked genre IDs
SELECT s.title AS title, g.genre_id AS genre_id
FROM tv_shows s INNER JOIN tv_show_genres g 
ON s.id = g.show_id
ORDER BY s.title, g.genre_id.
