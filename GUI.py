from settings import *
from os import path







class MainMenu():
    def __init__(self, game):
        self.game = game
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')





class PauseScreen():
    def __init__(self, game):
        self.game = game
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')









class BattleScreen():
    def __init__(self, game):
        self.game = game
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')
        self.location = None
        self.layer_1 = None
        self.layer_2 = menu_imgs['battle_menu_back']



    def Locate(self, location):
        if location == 'forest_encounter':
            self.layer_1 = menu_imgs['Foreset_battleback']

        if location == 'grasslands_encounter':
            self.layer_1 = menu_imgs['Grasslands_battleback']

        if location == 'mountains_encounter':
            self.layer_1 = menu_imgs['Mountains_battleback']

        if location == 'swamp_encounter':
            self.layer_1 = menu_imgs['Swamp_battleback']








