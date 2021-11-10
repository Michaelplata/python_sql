import pdb
from db.run_sql import run_sql
from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository

def create(album):
    sql = "INSERT INTO albums (title, artist_id, genre) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.artist.id, album.genre]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def delet_all():
    sql = 'DELETE FROM albums'
    run_sql(sql)


def select(id):
    album = None
    
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)[0]
    
    if results is not None:
        artist = artist_repository.select(results['artist_id'])
        album = Album(results['title'], artist, results['genre'], results['artist_id'])
    return album