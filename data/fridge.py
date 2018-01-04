# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 14:45:47 2017
Samo test da vidin kako funkcionira gutgab i source tree-
@author: Lorango
"""
import pygame
import natrix

sprite_1 = natrix.Sprite('test_3', 'grafics/slova4.png', (10, 10), 0.75)
sprite_2 = natrix.Sprite('slike', 'grafics/slike2.png', (30, 5), 0.75)

class Goi(natrix.predmet.PredmetSprite):
    def __init__(self, topleft=(200, 200), room_name='room_0', image_index=0):
        natrix.predmet.PredmetSprite.__init__(self, sprite_1, topleft)

        self.room_name = room_name
        self.image_index = image_index
        natrix.group_sprite.add(self)

    def lmb_down(self):
        natrix.goto_room(self.room_name)

class Full_screen(natrix.predmet.PredmetSprite):
    def __init__(self, topleft=(200, 200), image_index=0):
        natrix.predmet.PredmetSprite.__init__(self, sprite_1, topleft)

        self.image_index = image_index
        natrix.group_sprite.add(self)

    def lmb_down(self):
        natrix.full_screen = not(natrix.full_screen)
        if natrix.full_screen:
            pygame.display.set_mode(natrix.rez, pygame.FULLSCREEN)
        else:
            pygame.display.set_mode(natrix.rez)

class Ugasi(natrix.predmet.PredmetSprite):
    def __init__(self, topleft=(200, 200), image_index=0):
        natrix.predmet.PredmetSprite.__init__(self, sprite_1, topleft)

        self.image_index = image_index
        natrix.group_sprite.add(self)

    def lmb_down(self):
        pygame.event.post(pygame.event.Event(12, {}))
        if natrix.full_screen:
            pass
        else:
            pygame.display.set_mode(natrix.rez)

class Save(natrix.predmet.PredmetSprite):
    def __init__(self, topleft=(200, 200), image_index=0):
        natrix.predmet.PredmetSprite.__init__(self, sprite_1, topleft)

        self.image_index = image_index
        natrix.group_sprite.add(self)

    def lmb_down(self):
        natrix.options[0][0][0].text = str(500)
        natrix.tree.write('test_xml.txt')




natrix.rooms['room_1'] = natrix.tools.Room()
natrix.rooms['room_2'] = natrix.tools.Room()
natrix.rooms['room_3'] = natrix.tools.Room()
natrix.rooms['room_options'] = natrix.tools.Room()
natrix.rooms['room_res'] = natrix.tools.Room()

natrix.rooms['room_0'].clsarg.append((Save, {'topleft': (900, 50),
                                            'image_index': 33}))

natrix.rooms['room_0'].clsarg.append((Full_screen, {'topleft': (1300, 50),
                                            'image_index': 29}))

natrix.rooms['room_0'].clsarg.append((Ugasi, {'topleft': (1300, 400),
                                            'image_index': 49}))

natrix.rooms['room_0'].clsarg.append((Goi, {'topleft': (100, 50),
                                            'room_name': 'room_1',
                                            'image_index': 1}))

natrix.rooms['room_0'].clsarg.append((Goi, {'topleft': (100, 350),
                                            'room_name': 'room_2',
                                            'image_index': 2}))

natrix.rooms['room_0'].clsarg.append((Goi, {'topleft': (100, 650),
                                            'room_name': 'room_3',
                                            'image_index': 3}))

natrix.rooms['room_0'].clsarg.append((Goi, {'topleft': (1350, 650),
                                            'room_name': 'room_options',
                                            'image_index': 4}))

natrix.rooms['room_1'].clsarg.append((Goi, {'topleft': (1350, 650),
                                            'room_name': 'room_0',
                                            'image_index': 0}))

natrix.rooms['room_2'].clsarg.append((Goi, {'topleft': (1350, 650),
                                            'room_name': 'room_0',
                                            'image_index': 0}))

natrix.rooms['room_3'].clsarg.append((Goi, {'topleft': (1350, 650),
                                            'room_name': 'room_0',
                                            'image_index': 0}))

natrix.rooms['room_options'].clsarg.append((Goi, {'topleft': (1350, 650),
                                            'room_name': 'room_0',
                                            'image_index': 0}))

natrix.rooms['room_options'].clsarg.append((Goi, {'topleft': (50, 50),
                                            'room_name': 'room_res',
                                            'image_index': 5}))

natrix.rooms['room_res'].clsarg.append((Goi, {'topleft': (1350, 650),
                                            'room_name': 'room_options',
                                            'image_index': 4}))

import data.game_one
#data.game_one.options = natrix.options[1]

import data.game_two
#data.game_two.options = natrix.options[2]

import data.game_three
#data.game_three.options = natrix.options[3]