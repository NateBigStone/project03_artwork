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
    #
    # try:
    #     new_artist = Artist(artist_name='nate johnson', email='nate@nate.com')
    #     new_artist.save()
    #     new_artwork = Artwork(artwork_name='nate beautiful art', price=20.33, artist=1)
    #     new_artwork.save()
    # except() as e:
    #     print(e)


def create_menu():

    menu_class = Menu()
    menu_class.add_option('1', 'Add Artist', add_artist)

    menu_class.add_option('Q', 'Quit', quit_program)

    return menu_class


def add_artist():
    try:
        new_artist = ui.add_artist_info()
        new_artist.save()
    except Exception as e:
        print(f'\n{e}\n')


def quit_program():
    ui.message('Good day to you!')


if __name__ == "__main__":
    main()

"""
functions:
add a new artist
search by artist for artwork
display all available artwork by an artist
add a new artwork
delete an artwork
change availability of an artwork
"""