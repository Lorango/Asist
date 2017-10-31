# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 14:45:47 2017

@author: Lorango
"""

import pygame
import natrix

natrix.load_image('data/images/balloon.png')
natrix.load_image(path='data/images/brendan.png')
natrix.load_image(path='data/images/grad.png')

sprite_0 = natrix.Sprite('test2')
sprite_1 = natrix.Sprite('test3', 'data/images/balloon.png', (0, 0, 50, 50), 2)


class Spike(natrix.predmet.PredmetSprite):
    def __init__(self):
        natrix.predmet.PredmetSprite.__init__(self, sprite_0, (300, 100))
        self.auto_animated = True

    def step(self):
        self.rect.center = pygame.mouse.get_pos()


class Balloon(natrix.predmet.PredmetSprite):
    def __init__(self, player, topleft=(200, 200)):
        natrix.predmet.PredmetSprite.__init__(self, sprite_1, topleft)
        self.timer = 0
    pass

    def step(self):
        if self.rect.colliderect(player.rect):
            self.image_index = 1
        else:
            if self.image_index == 1 and self.timer < 30:
                self.timer += 1
            else:
                self.timer = 0
                self.image_index = 0

player = Spike()
natrix.group_sprite.add(natrix.predmet.PredmetSprite(sprite_0, (200, 100)))
natrix.group_sprite.add(player)
for i in range(9):
    natrix.group_sprite.add(Balloon(player, (60*(i//3), 60*(i % 3))))
