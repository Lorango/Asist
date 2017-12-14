# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 14:45:47 2017
Samo test da vidin kako funkcionira gutgab i source tree-
@author: Lorango
"""
import random
import pygame
import natrix


sprite_1 = natrix.Sprite('test3', 'grafics/slova02.png', (10, 10))


class Igra(natrix.predmet.PredmetSprite):
    def __init__(self, topleft=(200, 200)):
        natrix.predmet.PredmetSprite.__init__(self, sprite_1, topleft)

        self.image_index = 0
        self.slova = []  # objekti koji se stišće
        #  generiranje i pozicioniranje slova na ekran
        for i in range(5):
            self.slova.append(Slovo(0, (100 + 330*(i % 5), 350), self))

        for i in self.slova:
            natrix.group_sprite.add(i)

        self.gen()

    def step(self):
        pass

    def gen(self):
        """Popunjavanje i odabir slova ke će se pojavit na ekran.

        """
        self.ras = [60, 89]  # raspon slova
        self.image_index = random.randint(*self.ras)
        self.indeksi = [self.image_index]  # sliži za odabir slova
        for i in range(4):
            r = random.randint(*self.ras)
            while r in self.indeksi:
                r = random.randint(*self.ras)

            self.indeksi.append(r)

        random.shuffle(self.indeksi)

        for i in range(5):
            self.slova[i].image_index = self.indeksi[i]


class Slovo(natrix.predmet.PredmetSprite):
    def __init__(self, i=0, topleft=(200, 200), parent=None):
        natrix.predmet.PredmetSprite.__init__(self, sprite_1, topleft)
        self.parent = parent
        self.image_index = i

    def lmb_down(self):
        if self.image_index == self.parent.image_index:
            print('Točno')
            self.parent.gen()
        else:
            print('Krivo', self.rect)


class Goi(natrix.predmet.PredmetSprite):
    def __init__(self, topleft=(200, 200), room_name='room_0', image_index=0):
        natrix.predmet.PredmetSprite.__init__(self, sprite_1, topleft)

        self.room_name = room_name
        self.image_index = image_index
        natrix.group_sprite.add(self)

    def lmb_down(self):
        natrix.goto_room(self.room_name)

for i in range(10):
    natrix.rooms['room_0'].clsarg.append((Goi, {'topleft': (420 + 310*(i % 4), 50 + 310*(i // 4)),
                                            'room_name': 'room_0',
                                            'image_index': 10*i + i}))

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

natrix.rooms['room_1'].clsarg.append((Igra, {'topleft': (400, 0)}))
natrix.rooms['room_1'].clsarg.append((Goi, {'topleft': (0, 0),
                                            'room_name': 'room_0',
                                            'image_index': 0}))

natrix.rooms['room_2'].clsarg.append((Igra, {'topleft': (30, 30)}))
natrix.rooms['room_2'].clsarg.append((Goi, {'topleft': (0, 0),
                                            'room_name': 'room_0',
                                            'image_index': 0}))

natrix.rooms['room_3'].clsarg.append((Igra, {'topleft': (600, 30)}))
natrix.rooms['room_3'].clsarg.append((Goi, {'topleft': (0, 0),
                                            'room_name': 'room_0',
                                            'image_index': 0}))
