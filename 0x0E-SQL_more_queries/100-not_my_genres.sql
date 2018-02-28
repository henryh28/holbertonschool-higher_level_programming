-- Lists all genres not linked to the show 'Dexter'

SELECT tv_genres.name FROM tv_genres
WHERE tv_genres.name NOT IN (
      SELECT tv_genres.name FROM tv_genres
      INNER JOIN tv_show_genres
      INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
      WHERE tv_shows.title = 'Dexter' 
      AND tv_genres.id = tv_show_genres.genre_id
)
ORDER BY tv_genres.name ASC;
