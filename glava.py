# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 14:45:47 2017

@author: Lorango
"""

import sys
import pygame
import natrix

g = natrix.sprite.Group()

for j in range(4):
    for i in range(8):
        a = natrix.sprite.Sprite((195*j, 65*i, 32, 64), None)
        natrix.Controller.group.add(a)


class Dummy(natrix.sprite.Sprite):
    def __init__(self, rect, image):
        natrix.sprite.Sprite.__init__(self, rect, image)
        self.speed = 5

    def step(self):
        self.rect.move_ip(self.speed, 0)
        if self.rect.left < 100 or self.rect.left > 600:
            self.speed *= -1

a = Dummy((110, 100, 100, 50), None)
g.add(a)
natrix.Controller.group.add(a)
natrix.Controller.camera.sprite = a

#  Main loop.
while True:
    natrix.Controller.clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    natrix.Controller.step()
    natrix.Controller.draw()

    pygame.display.update()
