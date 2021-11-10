import pdb
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist_repository.delet_all()
album_repository.delet_all()

artist_1 = Artist('LTJ Bukem')
artist_repository.create_artist(artist_1)

album_0 = Album('Progression Session', artist_1, "Electronic")
album_repository.create(album_0)
album_1 = Album("Logical Progression", artist_1, "Electronic")
album_repository.create(album_1)



# for artist in artist_repository.select_all():
#     print(artist.__dict__)

pdb.set_trace()