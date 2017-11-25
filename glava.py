# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 14:45:47 2017

@author: Lorango
"""

import sys
import pygame
import natrix
import data.fridge as fridge

natrix.rooms['room_0'].start()

#  Main loop.
while True:
    natrix.clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                for predmet in natrix.group_sprite:
                    if predmet.rect.collidepoint(event.pos):
                        predmet.lmb_up()
                        break

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for predmet in natrix.group_sprite:
                    if predmet.rect.collidepoint(event.pos):
                        predmet.lmb_down()
                        break

    natrix.step()
    natrix.draw()

    pygame.display.update()
