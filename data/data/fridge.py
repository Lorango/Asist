# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 14:45:47 2017

@author: Lorango
"""
import random
import pygame
import natrix

natrix.load_image('data/images/slova_mala.png')

sprite_1 = natrix.Sprite('test3', 'data/images/slova_mala.png',
                         (0, 0, 100, 100), 6)


class Igra(natrix.predmet.PredmetSprite):
    def __init__(self, topleft=(200, 200)):
        natrix.predmet.PredmetSprite.__init__(self, sprite_1, topleft)
        self.image_index = 3
        self.slova = []
        for i in range(5):
            self.slova.append(Slovo(i, (100 + 130*(i % 5), 200)))
            natrix.group_sprite.add(self.slova[-1])

    def step(self):
        pass

    def foo(self):
        self.image_index = random.randint(0, 4)


class Slovo(natrix.predmet.PredmetSprite):
    def __init__(self, i=0, topleft=(200, 200)):
        natrix.predmet.PredmetSprite.__init__(self, sprite_1, topleft)
        self.timer = 0
        self.image_index = i

#    def step(self):
#        if self.rect.collidepoint(pygame.mouse.get_pos()):
#            self.image_index = 1
#        else:
#            if self.image_index == 1 and self.timer < 30:
#                self.timer += 1
#            else:
#                self.timer = 0
#                self.image_index = 0

    def lmb_down(self):
        if self.image_index == igra.image_index:
            print('Točno')
            igra.foo()
        else:
            print('Krivo')
#        print('Kobila')

igra = Igra((350, 30))
natrix.group_sprite.add(igra)

#for i in range(9):
#    natrix.group_sprite.add(Slovo((100*(i//3), 100*(i % 3))))
