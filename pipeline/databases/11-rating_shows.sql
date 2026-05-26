--lists all shows by rating
SELECT tv_shows.title , sum(tv_show_ratings.rate) AS rating 
FROM tv_shows
JOIN tv_show_ratings ON tv_show_ratings.show_id = tv_shows.id
GROUP BY tv_shows.id
ORDER BY rating DESC;