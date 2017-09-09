import pygame as pg
from settings import *
from tilemap import collide_hit_rect
from os import path





def collide_with_walls(sprite, group, dir):
    if dir == 'x':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centerx > sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.left - sprite.hit_rect.width / 2
            if hits[0].rect.centerx < sprite.hit_rect.centerx:
                sprite.pos.x = hits[0].rect.right + sprite.hit_rect.width / 2
            sprite.vel.x = 0
            sprite.hit_rect.centerx = sprite.pos.x
    if dir == 'y':
        hits = pg.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if hits[0].rect.centery > sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.top - sprite.hit_rect.height / 2
            if hits[0].rect.centery < sprite.hit_rect.centery:
                sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.height / 2
            sprite.vel.y = 0
            sprite.hit_rect.centery = sprite.pos.y


def collide_with_event(sprite, group, dir):
    if dir == 'x':
        hits = pg.sprite.collide_rect(sprite,group)
        if hits:



            sprite.map_change = True
            sprite.map_change_dest = group.destination
            # play_map_background = group.destination
            # sprite.vel.x = 0
            # sprite.hit_rect.centerx = sprite.pos.x

    if dir == 'y':
        hits = pg.sprite.collide_rect(sprite,group)
        if hits:


            sprite.map_change = True
            sprite.map_change_dest = group.destination

            # play_map_background = group.destination
            # sprite.vel.y = 0
            # sprite.hit_rect.centery = sprite.pos.y


def collide_with_encounter(sprite, group, dir):
    if dir == 'x':
        hits = pg.sprite.collide_rect(sprite,group)
        if hits:
            sprite.game.battle.location = group.location
            sprite.game.game_state = game_states['battle']




    if dir == 'y':
        hits = pg.sprite.collide_rect(sprite,group)
        if hits:
            sprite.game.battle.location = group.location
            sprite.game.game_state = game_states['battle']






class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = PLAYER_LAYER
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')


        self.vel = vec(0, 0)
        self.pos = vec(x, y)
        self.frame = 1
        self.speed = PLAYER_SPEED
        self.player_img_1 = pg.image.load(path.join(img_folder, PLAYER_IMG_1))
        self.player_img_2 = pg.image.load(path.join(img_folder, PLAYER_IMG_2))
        self.player_img_3 = pg.image.load(path.join(img_folder, PLAYER_IMG_3))
        self.player_img_4 = pg.image.load(path.join(img_folder, PLAYER_IMG_4))
        self.player_img_5 = pg.image.load(path.join(img_folder, PLAYER_IMG_5))
        self.player_img_6 = pg.image.load(path.join(img_folder, PLAYER_IMG_6))
        self.player_img_7 = pg.image.load(path.join(img_folder, PLAYER_IMG_7))
        self.player_img_8 = pg.image.load(path.join(img_folder, PLAYER_IMG_8))
        self.player_img_9 = pg.image.load(path.join(img_folder, PLAYER_IMG_9))
        self.player_img_10 = pg.image.load(path.join(img_folder, PLAYER_IMG_10))
        self.player_img_11 = pg.image.load(path.join(img_folder, PLAYER_IMG_11))
        self.player_img_12 = pg.image.load(path.join(img_folder, PLAYER_IMG_12))

        self.image_dict_f = {1 : self.player_img_1,
                             2 : self.player_img_2,
                             3 : self.player_img_3}

        self.image_dict_b = {1 : self.player_img_4,
                             2 : self.player_img_5,
                             3 : self.player_img_6}

        self.image_dict_r = {1 : self.player_img_7,
                             2 : self.player_img_8,
                             3 : self.player_img_9}
        self.image_dict_l = {1 : self.player_img_10,
                             2 : self.player_img_11,
                             3 : self.player_img_12}

        self.image = self.image_dict_f[1]
        self.rect = self.image.get_rect().inflate(-5, -5)
        self.rect.center = (x, y)
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center



        self.map_change = False
        self.map_change_dest = 0

    def get_keys(self):
        self.vel = vec(0, 0)
        self.speed = PLAYER_SPEED

        if not self.game.loading:

            keys = pg.key.get_pressed()

            if keys[pg.K_LSHIFT]:
                self.speed = PLAYER_SPEED * 2
            if keys[pg.K_LEFT] or keys[pg.K_a]:
                self.vel = vec(-self.speed,0)
            if keys[pg.K_RIGHT] or keys[pg.K_d]:
                self.vel = vec(self.speed,0)
            if keys[pg.K_UP] or keys[pg.K_w]:
                self.vel = vec(0, -self.speed)
            if keys[pg.K_DOWN] or keys[pg.K_s]:
                self.vel = vec(0, self.speed)
            else:
                pass

    def animate(self):
        if self.frame == 4:
            self.frame = 1
        ####down
        if self.vel == vec(0, self.speed):
            self.image = self.image_dict_f[self.frame]
            self.frame += 1
        ###up
        if self.vel == vec(0, -self.speed):
            self.image = self.image_dict_b[self.frame]
            self.frame +=1
        ####right
        if self.vel == vec(self.speed, 0):
            self.image = self.image_dict_r[self.frame]
            self.frame += 1
        ###left
        if self.vel == vec(-self.speed, 0):
            self.image = self.image_dict_l[self.frame]
            self.frame += 1
        else:
            pass





    def update(self):
        self.get_keys()
        self.animate()
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self, self.game.walls, 'x')

        for event in self.game.event:
            collide_with_event(self, event, 'x')
            collide_with_event(self, event, 'y')
        for encounter in self.game.encounter:
            collide_with_encounter(self, encounter, 'x')
            collide_with_encounter(self, encounter, 'y')

        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls, 'y')



        self.rect.center = self.hit_rect.center



class Cursor(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self._layer = PLAYER_LAYER
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')
        self.select = False
        self.direction = None
        self.menu_change = False
        self.menu_destination = None
        self.speed = PLAYER_SPEED
        self.vel = vec(0, 0)
        self.pos = vec(x, y)

        self.image = pg.image.load(path.join(img_folder, CURSOR_IMG))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.hit_rect = CURSOR_HIT_RECT
        self.hit_rect.center = self.rect.center




    def get_keys(self):
        self.vel = vec(0, 0)
        self.speed = PLAYER_SPEED

        if not self.game.loading:

            keys = pg.key.get_pressed()

            if keys[pg.K_LSHIFT]:
                self.speed = PLAYER_SPEED * 2
            if keys[pg.K_LEFT] or keys[pg.K_a]:
                self.vel = vec(-self.speed,0)
            if keys[pg.K_RIGHT] or keys[pg.K_d]:
                self.vel = vec(self.speed,0)
            if keys[pg.K_UP] or keys[pg.K_w]:
                self.vel = vec(0, -self.speed)
            if keys[pg.K_DOWN] or keys[pg.K_s]:
                self.vel = vec(0, self.speed)
            else:
                pass

    def update(self):
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self, self.game.walls, 'x')



        if self.select:
            for event in self.game.event:
                collide_with_event(self, event, 'x')
                collide_with_event(self, event, 'y')


        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls, 'y')



        self.rect.center = self.hit_rect.center



class Obstacle(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pg.Rect(x, y, w, h)
        self.hit_rect = self.rect
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

class Event(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h, destination):
        self.groups = game.event
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pg.Rect(x, y, w, h)
        self.hit_rect = self.rect
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.destination = destination

class Encounter(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h, location):
        self.groups = game.encounter
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = pg.Rect(x, y, w, h)
        self.hit_rect = self.rect
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.location = location