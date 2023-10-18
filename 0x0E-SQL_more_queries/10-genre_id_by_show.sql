-- TASK: List all shows in the 'hbtn_0d_tvshows' database with at least one linked genre.
-- TASK: List all shows in the 'hbtn_0d_tvshows' database with at least one linked genre.

-- Use the 'hbtn_0d_tvshows' database
USE hbtn_0d_tvshows;


-- List shows with at least one linked genre
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
