# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 14:45:47 2017
Samo test da vidin kako funkcionira gutgab i source tree-
@author: Lorango
"""

import natrix

sprite_1 = natrix.Sprite('test_3', 'grafics/slova4.png', (10, 10))
sprite_2 = natrix.Sprite('slike', 'grafics/slike2.png', (30, 5))

class Goi(natrix.predmet.PredmetSprite):
    def __init__(self, topleft=(200, 200), room_name='room_0', image_index=0):
        natrix.predmet.PredmetSprite.__init__(self, sprite_1, topleft)

        self.room_name = room_name
        self.image_index = image_index
        natrix.group_sprite.add(self)

    def lmb_down(self):
        natrix.goto_room(self.room_name)

natrix.rooms['room_1'] = natrix.tools.Room()
natrix.rooms['room_2'] = natrix.tools.Room()
natrix.rooms['room_3'] = natrix.tools.Room()

natrix.rooms['room_0'].clsarg.append((Goi, {'topleft': (100, 50),
                                            'room_name': 'room_1',
                                            'image_index': 1}))

natrix.rooms['room_0'].clsarg.append((Goi, {'topleft': (100, 350),
                                            'room_name': 'room_2',
                                            'image_index': 2}))

natrix.rooms['room_0'].clsarg.append((Goi, {'topleft': (100, 650),
                                            'room_name': 'room_3',
                                            'image_index': 3}))


natrix.rooms['room_1'].clsarg.append((Goi, {'topleft': (0, 0),
                                            'room_name': 'room_0',
                                            'image_index': 0}))

#natrix.rooms['room_2'].clsarg.append((Igra, {'topleft': (30, 30)}))
natrix.rooms['room_2'].clsarg.append((Goi, {'topleft': (0, 0),
                                            'room_name': 'room_0',
                                            'image_index': 0}))

natrix.rooms['room_3'].clsarg.append((Goi, {'topleft': (0, 0),
                                            'room_name': 'room_0',
                                            'image_index': 0}))

import data.game_one
data.game_one.options = natrix.options[1]

import data.game_two
data.game_two.options = natrix.options[2]

import data.game_three
data.game_three.options = natrix.options[3]