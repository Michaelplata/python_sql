from pdb import run
from db.run_sql import run_sql

from models.artist import Artist

def create_artist(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)

    id = results[0]['id']
    artist.id = id
    return artist

def delet_all():
    sql = "DELETE FROM artists"
    run_sql(sql)


def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [artist.id]
    results = run_sql(sql, values)[0]

    if results is not None:
        artist = Artist[results['name'], results['id']]

    return artist







def select_all():
    artists = []
    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in artists:
        artitst = Artist(row['name'], row['id'])
        artists.append(artitst)
    return artists