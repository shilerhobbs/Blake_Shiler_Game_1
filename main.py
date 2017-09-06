import pygame as pg
import sys
from random import choice, random
from os import path
from settings import *
from sprites import *
from tilemap import *
from GUI import *



class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_data()
        self.state = 'intro'
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.walls = pg.sprite.Group()
        self.event = pg.sprite.Group()
        self.paused = False
        self.game_state = 'world map'
        self.last_game_state = None
        self.player = Player(self, 0, 0)
        self.cursor = Cursor(self, 0, 0)
        self.pause_screen = PauseScreen(self,self.game_state)

    def draw_text(self, text, font_name, size, color, x, y, align="topleft"):
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(**{align: (x, y)})
        self.screen.blit(text_surface, text_rect)

    def load_data(self):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')
        snd_folder = path.join(game_folder, 'snd')
        music_folder = path.join(game_folder, 'music')
        self.map_folder = path.join(game_folder, 'maps')
        self.title_font = path.join(img_folder, 'rawline-100.ttf')
        self.dim_screen = pg.Surface(self.screen.get_size()).convert_alpha()
        self.dim_screen.fill((0, 0, 0, 180))
        self.menu_imgs = {}
        self.battle_backs = {}
        for img in menu_imgs:
            self.menu_imgs[img] = pg.image.load(path.join(img_folder,menu_imgs[img]))
        for img in battle_backs:
            self.battle_backs[img] = pg.image.load(path.join(img_folder, battle_backs[img]))



    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.walls = pg.sprite.Group()
        self.event = pg.sprite.Group()

        # self.player = Player(self, 0, 0)
        # self.cursor = Cursor(self, 0, 0)

        self.map = TiledMap(path.join(self.map_folder, play_map_background))
        self.map_forground = TiledMap(path.join(self.map_folder, play_map_forground))
        self.map_img = self.map.make_map()
        self.map_img_forgound = self.map_forground.make_map()
        self.map.rect = self.map_img.get_rect()
        #self.map_img_forgound.rect = self.map_img_forgound.get_rect()
        for tile_object in self.map.tmxdata.objects:
            obj_center = vec(tile_object.x + tile_object.width / 2,
                             tile_object.y + tile_object.height / 2)
            if tile_object.name == 'player':

                self.player = Player(self, obj_center.x, obj_center.y)
            if tile_object.name == 'cursor':

                self.cursor = Cursor(self, obj_center.x, obj_center.y)
            if tile_object.name == 'wall':

                Obstacle(self, tile_object.x, tile_object.y,
                         tile_object.width, tile_object.height)

            if tile_object.name == 'event':
                Event(self, tile_object.x, tile_object.y,
                         tile_object.width, tile_object.height,
                      tile_object.properties['destination'])


        self.camera = Camera(self.map.width, self.map.height)


        self.draw_debug = False
        self.paused = False
        self.loading = False

    def map(self):

        self.map = TiledMap(path.join(self.map_folder, play_map_background))
        self.map_forground = TiledMap(path.join(self.map_folder, play_map_forground))
        self.map_img = self.map.make_map()
        self.map_img_forgound = self.map_forground.make_map()
        self.map.rect = self.map_img.get_rect()
        # self.map_img_forgound.rect = self.map_img_forgound.get_rect()
        for tile_object in self.map.tmxdata.objects:
            obj_center = vec(tile_object.x + tile_object.width / 2,
                             tile_object.y + tile_object.height / 2)
            if tile_object.name == 'player':
                self.player = Player(self, obj_center.x, obj_center.y)
            if tile_object.name == 'cursor':
                self.cursor = Cursor(self, obj_center.x, obj_center.y)
            if tile_object.name == 'wall':
                Obstacle(self, tile_object.x, tile_object.y,
                         tile_object.width, tile_object.height)

            if tile_object.name == 'event':
                Event(self, tile_object.x, tile_object.y,
                      tile_object.width, tile_object.height,
                      tile_object.properties['destination'])

        self.camera = Camera(self.map.width, self.map.height)

        self.draw_debug = False
        self.paused = False
        self.loading = False
        self.game_state = 'world_map'

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000.0  # fix for Python 2.x
            self.events()

            self.draw()

            self.update()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()
        self.camera.update(self.player)
        if self.paused:
            self.game_state = 'paused'





    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
        self.screen.fill(BGCOLOR)

        if self.game_state == 'world map':
            self.screen.blit(self.map_img, self.camera.apply(self.map))
            # self.draw_grid()
            for sprite in self.all_sprites:
                self.screen.blit(sprite.image, self.camera.apply(sprite))
                if self.draw_debug:
                    pg.draw.rect(self.screen, CYAN, self.camera.apply_rect(sprite.hit_rect), 1)

            # self.screen.blit(self.map_img_forground, self.camera.apply(self.map))

        if self.game_state == 'paused':
            self.screen.blit(self.pause_screen.back_ground,(0,0))
            self.screen.blit(self.pause_screen.button_bl,self.pause_screen.button_bl_loc)
            self.screen.blit(self.pause_screen.button_br, self.pause_screen.button_br_loc)
            self.screen.blit(self.pause_screen.button_tl, self.pause_screen.button_tl_loc)
            self.screen.blit(self.pause_screen.button_tr, self.pause_screen.button_tr_loc)
            self.screen.blit(self.pause_screen.cursor,self.pause_screen.cursor_loc)



        if self.draw_debug:
            for wall in self.walls:
                pg.draw.rect(self.screen, CYAN, self.camera.apply_rect(wall.rect), 1)

        if self.draw_debug:
            for event in self.event:
                pg.draw.rect(self.screen, ORANGE, self.camera.apply_rect(event.rect), 1)

        # if self.paused:
        #     self.screen.blit(self.dim_screen, (0, 0))
        #     self.draw_text("Paused", self.title_font, 105, RED, WIDTH / 2, HEIGHT / 2, align="center")
        pg.display.flip()

    def events(self):
        # catch all events here


        if self.player.map_change:

            global back, play_map_background
            back = map_dict[self.player.map_change_dest]
            play_map_background = back
            self.player.map_change = False
            self.loading = True
            self.new()

        if self.cursor.menu_change:

            back = map_dict[self.cursor.menu_change_dest]
            play_map_background = back
            self.cursor.menu_change = False
            self.loading = True
            self.new()
        # self.map = TiledMap(path.join(self.map_folder, play_map_background))
        # self.map_img = self.map.make_map()


        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_h:
                    self.draw_debug = not self.draw_debug
                if event.key == pg.K_p:
                    if not self.paused:
                        self.last_game_state = self.game_state
                        self.game_state = 'paused'
                        self.paused = True
                    if self.paused:
                        self.game_state = self.last_game_state
                        self.paused = False


    def show_start_screen(self):
        pass


    def show_go_screen(self):
        self.screen.fill(BLACK)
        self.draw_text("GAME OVER", self.title_font, 100, RED,
                       WIDTH / 2, HEIGHT / 2, align="center")
        self.draw_text("Press a key to start", self.title_font, 75, WHITE,
                       WIDTH / 2, HEIGHT * 3 / 4, align="center")
        pg.display.flip()
        self.wait_for_key()

        def wait_for_key(self):
            pg.event.wait()
            waiting = True
            while waiting:
                self.clock.tick(FPS)
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        waiting = False
                        self.quit()
                    if event.type == pg.KEYUP:
                        waiting = False

# create the game object
g = Game()
g.show_start_screen()
while True:
    g.new()
    g.run()
    g.show_go_screen()