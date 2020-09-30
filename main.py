import menu
from database import *


def main():
    try:
        new_artist = Artist(artist_name='nate johnson', email='nate@nate.com')
        new_artist.save()
        new_artwork = Artwork(artwork_name='nate beautiful art', price=20.33, artist=1)
        new_artwork.save()
    except() as e:
        print(e)
    print(menu.menu())


if __name__ == "__main__":
    main()

"""
database schemas:
artists
name, email
artworks
name(primary key), price, available, artist.id


fuctions:
add a new artist
search by artist for artwork
display all available artwork by an artist
add a new artwork
delete an artwork
change availability of an artwork
"""