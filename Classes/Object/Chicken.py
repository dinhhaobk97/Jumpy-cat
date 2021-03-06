##############################################
#	Assignment 3 - Game Programming - HK181
#
#   Group 4:
#   Pham Quang Minh - 1512016
#   Nguyen Dinh Hao - 1510896
#   Vu Anh Tuan - 1513888
############################################

import pygame as pg
from Classes.Constants import CHICKEN_DIR, BLACK
from random import choice
vec = pg.math.Vector2

class Chicken(pg.sprite.Sprite):
    def __init__(self, game, pos_x, pos_y):
        self.groups = game.all_sprites, game.chickens
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.pos_x = pos_x
        self.pos_y = pos_y

        #self.speed = choice([4, 5, 6])
        #self.pos_to_change_dir = choice([4000, 4500, 5000])
        self.speed = choice([5])
        self.pos_to_change_dir = choice([450])
        self.isRight = True

        self.current_frame = 0
        self.last_update = 0

        self.load_images()
        self.image = self.run_frame_r[0]

        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image) # Mask of chicken
        self.rect.x = pos_x
        self.rect.y = pos_y

        self.pos = vec(self.rect.x, self.rect.y) # Position of chicken
        self.movx = 0
        self.movy = 5

    def load_images(self):
        # Run state
        self.run_frame_r = [pg.transform.scale(pg.image.load(CHICKEN_DIR + "Chicken_1.png"), (int(331 * 0.3), int(300 * 0.3))),
                            pg.transform.scale(pg.image.load(CHICKEN_DIR + "Chicken_2.png"), (int(333 * 0.3), int(281 * 0.3))),
                            pg.transform.scale(pg.image.load(CHICKEN_DIR + "Chicken_3.png"), (int(368 * 0.3), int(247 * 0.3))),
                            pg.transform.scale(pg.image.load(CHICKEN_DIR + "Chicken_4.png"), (int(332 * 0.3), int(290 * 0.3))),
                            pg.transform.scale(pg.image.load(CHICKEN_DIR + "Chicken_5.png"), (int(334 * 0.3), int(274 * 0.3))),
                            pg.transform.scale(pg.image.load(CHICKEN_DIR + "Chicken_6.png"), (int(357 * 0.3), int(233 * 0.3)))]

        self.run_frame_l = []
        for img in range(0, len(self.run_frame_r)):
            self.run_frame_l.append(pg.transform.flip(self.run_frame_r[img], True, False))

    def update(self):
        now = pg.time.get_ticks() # Count time to change frames

        self.pos.y += self.movy   

        if self.isRight:
            self.pos.x += self.speed
            if now - self.last_update > 100:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.run_frame_r)
                    
                self.image = self.run_frame_r[self.current_frame]
         
                if self.pos.x - self.pos_x > self.pos_to_change_dir:
                    self.isRight = False
        
        else:
            self.pos.x -= self.speed
            if now - self.last_update > 100:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.run_frame_l)
                    
                self.image = self.run_frame_l[self.current_frame]
               
                if self.pos_x - self.pos.x > self.pos_to_change_dir:
                    self.isRight = True

        self.rect.center = self.pos