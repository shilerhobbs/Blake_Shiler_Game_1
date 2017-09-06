import pygame as pg
from settings import *
from os import path







class MainMenu():
    def __init__(self, game, last_game_state):
        self.game = game
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')
        self.last_game_state = last_game_state
        self.puased = False
        self.direction = None
        self.position = position['top_left']
        self.select = False
        self.back_ground = game.menu_imgs['Menu_background']
        self.button_tl = game.menu_imgs['Start_button']
        self.button_tl_loc = (22,175)
        self.button_tr = game.menu_imgs['continue_button']
        self.button_tr_loc = (251,175)
        self.button_bl = game.menu_imgs['Credits_button']
        self.button_bl_loc = (22,248)
        self.button_br = game.menu_imgs['Quit_button']
        self.button_br_loc = (251,248)
        self.cursor = game.menu_imgs['Cursor']
        self.cursor_loc = (22,189)
        self.cursor_pos_tl = (22,189)
        self.cursor_pos_tr = (251, 189)
        self.cursor_pos_bl = (22, 262)
        self.cursor_pos_br = (251, 262)


        # 14 pixels under   -= (0,14)

    def get_keys(self):
        keys = pg.key.get_pressed()


        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.direction = direction['left']
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.direction = direction['right']
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.direction = direction['up']
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.direction = direction['down']
        if keys[pg.K_SPACE]:
            self.select = True
        else:
            pass


    def update(self):
        self.get_keys()

        if self.select:
            if self.position == position['top_left']:
                self.game.game_state = game_states['world map']

        if self.direction == direction['left']:
            if self.position == position['top_right']:
                self.cursor_loc = self.cursor_pos_tl
                self.position = position['top_left']
            if self.position == position['bottom_right']:
                self.cursor_loc = self.cursor_pos_bl
                self.position = position['bottom_left']
            else:
                pass

        if self.direction == direction['right']:
            if self.position == position['top_left']:
                self.cursor_loc = self.cursor_pos_tr
                self.position = position['top_right']
            if self.position == position['bottom_left']:
                self.cursor_loc = self.cursor_pos_br
                self.position = position['bottom_right']
            else:
                pass

        if self.direction == direction['up']:
            if self.position == position['bottom_left']:
                self.cursor_loc = self.cursor_pos_tl
                self.position = position['top_left']
            if self.position == position['bottom_right']:
                self.cursor_loc = self.cursor_pos_tr
                self.position = position['top_right']
            else:
                pass

        if self.direction == direction['down']:
            if self.position == position['top_left']:
                self.cursor_loc = self.cursor_pos_bl
                self.position = position['bottom_left']
            if self.position == position['top_right']:
                self.cursor_loc = self.cursor_pos_br
                self.position = position['bottom_right']
            else:
                pass


        else:
            pass





class PauseScreen():
    def __init__(self, game, last_game_state):
        self.game = game
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')
        self.last_game_state = None
        self.puased = False
        self.direction = None
        self.position = position['top_left']
        self.select = False
        self.back_ground = game.menu_imgs['Menu_background']
        self.button_tl = game.menu_imgs['inventory_button']
        self.button_tl_loc = (22,175)
        self.button_tr = game.menu_imgs['character_button']
        self.button_tr_loc = (251,175)
        self.button_bl = game.menu_imgs['journal_button']
        self.button_bl_loc = (22,248)
        self.button_br = game.menu_imgs['Quit_button']
        self.button_br_loc = (251,248)
        self.cursor = game.menu_imgs['Cursor']
        self.cursor_loc = (22,189)
        self.cursor_pos_tl = (22,189)
        self.cursor_pos_tr = (251, 189)
        self.cursor_pos_bl = (22, 262)
        self.cursor_pos_br = (251, 262)


        # 14 pixels under   -= (0,14)

    def get_keys(self):
        keys = pg.key.get_pressed()


        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.direction = direction['left']
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.direction = direction['right']
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.direction = direction['up']
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.direction = direction['down']
        if keys[pg.K_SPACE]:
            self.select = True
        else:
            pass


    def update(self):
        self.get_keys()

        if self.select:
            pass

        if self.direction == direction['left']:
            if self.position == position['top_right']:
                self.cursor_loc = self.cursor_pos_tl
                self.position = position['top_left']
            if self.position == position['bottom_right']:
                self.cursor_loc = self.cursor_pos_bl
                self.position = position['bottom_left']
            else:
                pass

        if self.direction == direction['right']:
            if self.position == position['top_left']:
                self.cursor_loc = self.cursor_pos_tr
                self.position = position['top_right']
            if self.position == position['bottom_left']:
                self.cursor_loc = self.cursor_pos_br
                self.position = position['bottom_right']
            else:
                pass

        if self.direction == direction['up']:
            if self.position == position['bottom_left']:
                self.cursor_loc = self.cursor_pos_tl
                self.position = position['top_left']
            if self.position == position['bottom_right']:
                self.cursor_loc = self.cursor_pos_tr
                self.position = position['top_right']
            else:
                pass

        if self.direction == direction['down']:
            if self.position == position['top_left']:
                self.cursor_loc = self.cursor_pos_bl
                self.position = position['bottom_left']
            if self.position == position['top_right']:
                self.cursor_loc = self.cursor_pos_br
                self.position = position['bottom_right']
            else:
                pass


        else:
            pass










class BattleScreen():
    def __init__(self, game):
        self.game = game
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')
        self.location = None
        self.select = False
        self.position = None
        self.direction = None
        self.cursor = game.menu_imgs['small cursor']
        self.cursor_loc = (-2,269)
        self.cursor_pos_tl = (-2,269)
        self.cursor_pos_tr = (121,269)
        self.cursor_pos_bl = (-2,295)
        self.cursor_pos_br = (121,295)

        self.layer_1 = game.battle_backs['Mountains_battleback']

        self.layer_2 = game.menu_imgs['battle_menu_back']
        self.layer_2_loc = (0,264)
        self.button_1 = game.menu_imgs['attack_button']
        self.button_1_loc = (-3,261)
        self.button_2 = game.menu_imgs['Item_button']
        self.button_2_loc = (114,261)
        self.button_3 = game.menu_imgs['Equip_button']
        self.button_3_loc = (-3,287)
        self.button_4 = game.menu_imgs['Flee_button']
        self.button_4_loc = (114,287)



    def Locate(self, location):
        if location == 'forest_encounter':
            self.layer_1 = self.game.battle_backs['Foreset_battleback']

        if location == 'grasslands_encounter':
            self.layer_1 = self.game.battle_backs['Grasslands_battleback']

        if location == 'mountains_encounter':
            self.layer_1 = self.game.battle_backs['Mountains_battleback']

        if location == 'swamp_encounter':
            self.layer_1 = self.game.battle_backs['Swamp_battleback']


    def get_keys(self):
        keys = pg.key.get_pressed()


        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.direction = direction['left']
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.direction = direction['right']
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.direction = direction['up']
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.direction = direction['down']
        if keys[pg.K_SPACE]:
            self.select = True
        else:
            pass


    def update(self):
        self.get_keys()

        if self.select:
            pass

        if self.direction == direction['left']:
            if self.position == position['top_right']:
                self.cursor_loc = self.cursor_pos_tl
                self.position = position['top_left']
            if self.position == position['bottom_right']:
                self.cursor_loc = self.cursor_pos_bl
                self.position = position['bottom_left']
            else:
                pass

        if self.direction == direction['right']:
            if self.position == position['top_left']:
                self.cursor_loc = self.cursor_pos_tr
                self.position = position['top_right']
            if self.position == position['bottom_left']:
                self.cursor_loc = self.cursor_pos_br
                self.position = position['bottom_right']
            else:
                pass

        if self.direction == direction['up']:
            if self.position == position['bottom_left']:
                self.cursor_loc = self.cursor_pos_tl
                self.position = position['top_left']
            if self.position == position['bottom_right']:
                self.cursor_loc = self.cursor_pos_tr
                self.position = position['top_right']
            else:
                pass

        if self.direction == direction['down']:
            if self.position == position['top_left']:
                self.cursor_loc = self.cursor_pos_bl
                self.position = position['bottom_left']
            if self.position == position['top_right']:
                self.cursor_loc = self.cursor_pos_br
                self.position = position['bottom_right']
            else:
                pass


        else:
            pass




