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
radius = 30
def_pos = [-100, -100]
pos = def_pos
dwell = True
period = 1000

#  Main loop.
while True:
    natrix.clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.quit()
            pygame.quit()
            sys.exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == 100:
                if natrix.room_t == 'room_options':
                    natrix.options[0][1].text = str(int(not(int(natrix.options[0][1].text))))
                    if int(natrix.options[0][1].text):
                        pygame.time.set_timer(26, period)
                        pos = pygame.mouse.get_pos()
                        dwell = True
                    else:
                        pygame.time.set_timer(26, 0)
                        pos = def_pos
                        dwell = False

        if event.type == pygame.MOUSEMOTION:
            if int(natrix.options[0][1].text):
                x, y = event.pos
                r = ((pos[0] - x)**2 + (pos[1] - y)**2)**0.5  # filter
                if r > radius:
                    pos = event.pos
                    dwell = True
                else:
                    if dwell:
                        pygame.time.set_timer(26, period)
                        dwell = False
            else:
                pygame.time.set_timer(26, 0)
                pos = def_pos
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
    pygame.draw.circle(natrix.screen, natrix.red, pos, radius, 1)


    pygame.display.update()
