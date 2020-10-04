from menu import Menu
import ui
from database import *


def main():

    new_menu = create_menu()

    while True:
        choice = ui.display_menu_get_choice(new_menu)
        action = new_menu.get_action(choice)
        action()
        if choice == 'Q':
            break


def create_menu():

    menu_class = Menu()
    menu_class.add_option('1', 'Add Artist', add_artist)
    menu_class.add_option('2', 'Search for All Artworks by an Artist', search_artist_all)
    menu_class.add_option('3', 'Search for Available Artworks by Artist', search_artist_available)
    menu_class.add_option('T', 'Generate Test Tables', generate_test_tables)
    menu_class.add_option('D', 'Drop Test Tables', drop_test_tables)
    menu_class.add_option('Q', 'Quit', quit_program)

    return menu_class


def add_artist():
    try:
        new_artist = ui.add_artist_info()
        new_artist.save()
    except Exception as e:
        ui.message(e)


def search_artist_all():
    try:
        artist_msg = 'Enter artist name:\n'
        art_results = ui.artist_query(artist_msg)
        if art_results:
            ui.message(ui.print_artwork(art_results))
        else:
            ui.message('No artworks found by this artist.')
    except Exception as e:
        ui.message(e)


def search_artist_available():
    try:
        artist_msg = 'Enter artist name:\n'
        art_results = ui.artist_query(artist_msg, False)
        if art_results:
            ui.message(ui.print_artwork(art_results))
        else:
            ui.message('No artwork matches your query.')
    except Exception as e:
        ui.message(e)


def generate_test_tables():
    try:
        new_artist_1 = Artist(artist_name='nate johnson', email='nate@nate.com')
        new_artist_1.save()
        new_artist_2 = Artist(artist_name='Nate', email='coolguy123@yahoo.com')
        new_artist_2.save()
        new_artist_3 = Artist(artist_name='Nick Gant', email='nick86@aol.com')
        new_artist_3.save()
        new_artwork_1 = Artwork(artwork_name='nate beautiful art', price=20.33, artist=2)
        new_artwork_1.save()
        new_artwork_2 = Artwork(artwork_name='best code ever', price=1.30, artist=2)
        new_artwork_2.save()
        new_artwork_3 = Artwork(artwork_name='Sold Artwork', price=700.9, available=False, artist=2)
        new_artwork_3.save()
    except Exception as e:
        ui.message(e)


def drop_test_tables():
    db.drop_tables([Artist, Artwork])


def quit_program():
    ui.message('Good day to you!')


if __name__ == "__main__":
    main()

#TODO:
"""
add a new artwork ->enter artist. is artist? ask for values. ask to save
delete an artwork
change availability of an artwork
tests

refactor:
make it so that the artist query isn't case sensitive
validate input: artist email, price. 
hide admin options
Use Pandas for printouts?
"""
