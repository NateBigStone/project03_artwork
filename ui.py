from database import *


def display_menu_get_choice(menu):
    while True:
        print(menu)
        choice = input('Enter choice:\n').upper().strip()
        if menu.is_valid(choice):
            return choice
        else:
            message("Invalid choice, try again.")


def add_artist_info():
    artist_name = input('Enter artist name:\n')
    email = input('Enter artist email:\n')
    return Artist(artist_name=artist_name, email=email)


def artist_query(msg, all_art=True):
    get_search = input(msg)
    art_list = []
    query = Artwork.select().join(Artist).where(Artist.artist_name == get_search).dicts()
    if not all_art:
        query = query.where(Artwork.available)
    for art in query:
        art_list.append(art)
    return art_list


def print_artwork(artworks):
    art_string = ''
    for art in artworks:
        art_string += \
            f'\"{art["artwork_name"]}\"\t\t${art["price"]:.2f}\t' \
            f'{"Available" if art["available"] else "Sold"}\n'
    return art_string


def message(msg):
    print(f'\n{msg}\n')
