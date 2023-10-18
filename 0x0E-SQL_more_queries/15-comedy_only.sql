-- Task: List shows of a specific genre (Comedy).
-- Retrieve titles of Comedy shows, ordered by show title.
SELECT s.title
FROM tv_genres g
INNER JOIN tv_show_genres sg ON g.id = sg.genre_id
INNER JOIN tv_shows s ON sg.show_id = s.id
WHERE g.name = 'Comedy'
ORDER BY s.title;
