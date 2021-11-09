import pdb
from models.artists import Artist
import repositories.artist_repository as artist_repository

artist_1 = Artist("LTJ Bukem")

artist_repository.create_artist(artist_1)