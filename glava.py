# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 14:45:47 2017

@author: Lorango
"""

import sys
import pygame
import natrix
import data.data.fridge as fridge

#natrix.load_image('data/images/balloon.png')
#natrix.load_image(path='data/images/brendan.png')

g = natrix.predmet.Group()

for j in range(4):
    for i in range(8):
        a = natrix.predmet.Predmet((195*j, 65*i, 32, 64), None)
        natrix.group.add(a)


class Dummy(natrix.predmet.Predmet):
    def __init__(self, rect, image_name):
        natrix.predmet.Predmet.__init__(self, rect, image_name)
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
natrix.camera.predmet = a

#  Main loop.
t = 0
while True:
    natrix.clock.tick(30)
    t += 1
    if t > 2:
        t = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                for predmet in natrix.group_gui:
                    if predmet.rect.collidepoint(event.pos):
                        predmet.lmb_up()
                        break

    natrix.step()
    natrix.draw()
    natrix.screen.blit(natrix.images['data/images/grad.png'], pygame.mouse.get_pos(), None, pygame.BLEND_MULT)


    pygame.display.update()
