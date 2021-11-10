DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;

CREATE TABLE artists (
    id serial PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE albums (
    id serial PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    genre VARCHAR(255),
    artist_id INT REFERENCES artists(id)
);
    
