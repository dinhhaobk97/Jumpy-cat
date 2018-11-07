##############################################
#	Assignment 3 - Game Programming - HK181
#
#   Group 4:
#   Pham Quang Minh - 1512016
#   Nguyen Dinh Hao - 1510896
#   Vu Anh Tuan - 1513888
############################################

import pygame as pg
from random import choice
from Classes.Constants import ITEM_DIR, BLACK

class Item(pg.sprite.Sprite):
    def __init__(self, game, pos_x, pos_y, type):
        self.groups = game.all_sprites, game.items
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        self.item_list = [pg.transform.scale(pg.image.load(ITEM_DIR + "Tree.png"), (600, 600)),
                            pg.transform.scale(pg.image.load(ITEM_DIR + "Tree_2.png"), (600, 600))]

        self.image = choice(self.item_list)
        self.image.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y