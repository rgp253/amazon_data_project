-- The name of the file after exporting is "final_clean_movies.csv"

DELETE FROM amazon_movies WHERE rowid NOT IN(
    SELECT MAX(rowid) FROM amazon_movies GROUP BY movie_name, language);
    
SELECT * FROM amazon_movies;