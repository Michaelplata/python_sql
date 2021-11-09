from pdb import run
from db.run_sql import run_sql

from models.artists import Artist

def create_artist(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)

    id = results[0]['id']
    artist.id = id
    return artist