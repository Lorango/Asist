# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 16:31:46 2018

@author: Lorango
"""
import pygame
import natrix

res = [[(1280, 720), (1366, 768), (1600, 900), (1920, 1080)],
       [(1280, 800), (1440, 900), (1680, 1050), (1920, 1200)],
       [(800, 600), (1024, 786), (1152, 864), (1600, 1200)],
       [(800, 480), (1280, 768), (1280, 1024)]]

class Btn_rez(natrix.predmet.PredmetSprite):
    def __init__(self,
                 topleft=(200, 200),
                 room_name='room_0',
                 image_index=0,
                 res=(800, 600)):

        natrix.predmet.PredmetSprite.__init__(self,
                                              natrix.sprites['test_3'],
                                              topleft)

        self.room_name = room_name
        self.image_index = image_index
        self.res = res
        natrix.group_sprite.add(self)

    def lmb_down(self):
        natrix.options[0][0][0].text = str(self.res[0])
        natrix.options[0][0][1].text = str(self.res[1])
#        natrix.rez = list(self.res)
#        pygame.display.set_mode(natrix.rez, pygame.FULLSCREEN)
#        print(self.res)
        natrix.goto_room(self.room_name)
##



for j, ratio in enumerate(res):
    for i, r_ in enumerate(ratio):
        natrix.rooms['room_res'].clsarg.append((Btn_rez,
                                            {'topleft': (50 + 350 * i, 230 * j),
                                             'room_name': 'room_options',
                                             'image_index': 60+i+5*j,
                                             'res': r_}))
