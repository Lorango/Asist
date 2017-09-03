# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 14:45:47 2017

@author: Lorango
"""

import sys
import pygame
import natrix

natrix.load_image('data/images/cat.png')

g = natrix.sprite.Group()

for j in range(4):
    for i in range(8):
        a = natrix.sprite.Sprite((195*j, 65*i, 32, 64), None)
        natrix.group.add(a)


class Dummy(natrix.sprite.Sprite):
    def __init__(self, rect, image_name):
        natrix.sprite.Sprite.__init__(self, rect, image_name)
        self.speed = 5

        self.string_var = natrix.gui.StringVar(self.rect.left)

    def step(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.left < 100 or self.rect.left > 600:
            self.speed *= -1

        self.string_var._set(self.rect.left)

a = Dummy((110, 100, 100, 50), None)
g.add(a)
natrix.group.add(a)
natrix.camera.sprite = a

natrix.group_gui.add(natrix.gui.Button((10, 10, 50, 50), natrix.gui.kobila, {'a': 2, 'b': 3}, 'data/images/cat.png'))
natrix.group_gui.add(natrix.gui.Label())
natrix.group_gui.add(natrix.gui.Label((10, 100, 10, 10), string_var=a.string_var))

#  Main loop.
while True:
    natrix.clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                for sprite in natrix.group_gui:
                    if sprite.rect.collidepoint(event.pos):
                        sprite.lmb_up()
                        break

    natrix.step()
    natrix.draw()

    pygame.display.update()
