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

class Btn_gn(natrix.predmet.PredmetSprite):
    """broj odgovora

    """
    def __init__(self,
                 topleft=(200, 200),
                 game=1,
                 image_index=0):

        natrix.predmet.PredmetSprite.__init__(self,
                                              natrix.sprites['test_3'],
                                              topleft)


        self.game = game
        self.image_index = int(natrix.options[self.game][0].text)
        natrix.group_sprite.add(self)

    def lmb_down(self):
        self.image_index += 1
        if self.image_index > 5:
            self.image_index = 3

        natrix.options[self.game][0].text = str(self.image_index)

class Btn_gopcija(natrix.predmet.PredmetSprite):
    """pali gasi opciju

    """
    def __init__(self,
                 topleft=(200, 200),
                 game=1,
                 opcija_id=1,
                 image_index=0):

        natrix.predmet.PredmetSprite.__init__(self,
                                              natrix.sprites['test_3'],
                                              topleft)


        self.game = game
        self.opcija_id = opcija_id
        self.value = int(natrix.options[self.game][self.opcija_id].text)
        self.image_index = self.value*10 + 60
        natrix.group_sprite.add(self)

    def lmb_down(self):
        self.value = not(self.value)
        self.image_index = self.value*10 + 60

        natrix.options[self.game][self.opcija_id].text = str(int(self.value))
        print(len(natrix.options[self.game]))
##


for j, ratio in enumerate(res):
    for i, r_ in enumerate(ratio):
        natrix.rooms['room_res'].clsarg.append((Btn_rez,
                                            {'topleft': (50 + 350 * i, 230 * j),
                                             'room_name': 'room_options',
                                             'image_index': 60+i+5*j,
                                             'res': r_}))

# room game options 1 =================
natrix.rooms['room_opt_1'].clsarg.append((Btn_gn,
                                         {'topleft': (50, 50),
                                          'game': 1,
                                          'image_index': int(natrix.options[1][0].text)}))

for i in range(1, 5):
    natrix.rooms['room_opt_1'].clsarg.append((Btn_gopcija,
                                             {'topleft': (50 + 280 * (i-1), 280),
                                              'game': 1,
                                              'opcija_id': i}))

natrix.rooms['room_opt_1'].clsarg.append((Btn_gopcija,
                                             {'topleft': (50 + 280 * 2, 610),
                                              'game': 1,
                                              'opcija_id': 5}))


# room game options 3 =================
natrix.rooms['room_opt_3'].clsarg.append((Btn_gn,
                                         {'topleft': (50, 50),
                                          'game': 3,
                                          'image_index': int(natrix.options[3][0].text)}))

for i in range(1, 7):
    natrix.rooms['room_opt_3'].clsarg.append((Btn_gopcija,
                                             {'topleft': (50 + 260 * (i-1), 280),
                                              'game': 3,
                                              'opcija_id': i}))










