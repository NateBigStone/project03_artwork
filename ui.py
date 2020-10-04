from database import *


def display_menu_get_choice(menu):
    while True:
        print(menu)
        choice = input('Enter choice:\n').upper().strip()
        if menu.is_valid(choice):
            return choice
        else:
            print("Invalid choice, try again.")


def add_artist_info():
    artist_name = input('Enter artist name:\n')
    email = input('Enter artist email:\n')
    return Artist(artist_name=artist_name, email=email)


def message(msg):
    print(msg)
