import pygame as pg
from settings import *
from os import path







class MainMenu():
    def __init__(self, game):
        self.game = game
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')





class PauseScreen():
    def __init__(self, game, last_game_state):
        self.game = game
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')
        self.last_game_state = last_game_state
        self.puased = False
        self.direction = None
        self.position = 'top_left'
        self.select = False
        self.back_ground = game.menu_imgs['Menu_background']
        self.button_tl = game.menu_imgs['Start_button']
        self.button_tl_loc = (0,0)
        self.button_tr = game.menu_imgs['continue_button']
        self.button_tr_loc = (0,0)
        self.button_bl = game.menu_imgs['Credits_button']
        self.button_bl_loc = (0,0)
        self.button_br = game.menu_imgs['Quit_button']
        self.button_br_loc = (0,0)
        self.cursor = game.menu_imgs['Cursor']
        self.cursor_loc = (0,0)

    def get_keys(self):
        keys = pg.key.get_pressed()


        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.direction = 'left'
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.direction = 'right'
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.direction = 'up'
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.direction = 'down'
        if keys[pg.K_SPACE]:
            self.select = True
        else:
            self.direction = None
            self.select = False


    def update(self):
        if self.select:
            pass

        if self.direction == 'left':
            if self.position == 'top_left':
                pass
            if self.position == 'top_right':
                self.position = 'top_left'
            if self.position == 'bottom_left':
                pass
            if self.position == 'bottom_right':
                self.position = 'bottom_left'

        if self.direction == 'right':
            if self.position == 'top_left':
                self.position = 'top_right'
            if self.position == 'top_right':
                pass
            if self.position == 'bottom_left':
                self.position = 'bottom_right'
            if self.position == 'bottom_right':
                pass

        if self.direction == 'up':
            if self.position == 'top_left':
                pass
            if self.position == 'top_right':
                pass
            if self.position == 'bottom_left':
                self.position = 'top_left'
            if self.position == 'bottom_right':
                self.position = 'top_right'

        if self.direction == 'down':
            if self.position == 'top_left':
                self.position = 'bottom_left'
            if self.position == 'top_right':
                self.position = 'bottom_right'
            if self.position == 'bottom_left':
                pass
            if self.position == 'bottom_right':
                pass

        else:
            pass









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








