# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 14:45:47 2017

@author: Lorango
"""

import sys
import pygame
import natrix
import data.fridge


natrix.rooms['room_0'].start()
# dwell parametri
pos = [0, 0]
dwell = True

#  Main loop.
while True:
    natrix.clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.quit()
            pygame.quit()
            sys.exit(0)

        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            r = ((pos[0] - x)**2 + (pos[1] - y)**2)**0.5  # filter
            if r > 30:
                pos = event.pos
                dwell = True
            else:
                if dwell:
                    pygame.time.set_timer(26, 1000)
                    dwell = False


        if event.type == 26:
            attributes = {'button': 1, 'pos': pos}
            ev = pygame.event.Event(5,  attributes)
            pygame.event.post(ev)


        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                for predmet in natrix.group_sprite:
                    if predmet.rect.collidepoint(event.pos):
                        predmet.lmb_up()
                        break

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event)
            if event.button == 1:
                for predmet in natrix.group_sprite:
                    if predmet.rect.collidepoint(event.pos):
                        # original
                        # predmet.lmb_down()
                        # break
                        # patch
                        # Nemore stisnut na botune dokle se izgovara zadatak
                        if type(predmet) == data.fridge.Goi:
                            predmet.lmb_down()
                        elif not(natrix.kanal.get_busy()):
                            predmet.lmb_down()
                        break

        if event.type == 25:
            natrix.kond.update_queue()

    natrix.step()
    natrix.draw()
    # dwel klik radius
    pygame.draw.circle(natrix.screen, natrix.red, pos, 30, 5)


    pygame.display.update()
