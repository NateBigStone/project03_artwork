"""
Inspired by the reading list menu
"""


class Menu:

    def __init__(self):
        self.menu_options = {}
        self.functions = {}

    def add_option(self, key, description, function):
        self.menu_options[key] = description
        self.functions[key] = function

    def is_valid(self, choice):
        return choice in self.menu_options

    def get_action(self, choice):
        return self.functions.get(choice)

    def __str__(self):
        texts = [f'{key}: {self.menu_options[key]}' for key in self.menu_options.keys()]
        return '\n'.join(texts)
