# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 13:53:52 2017

@author: Lorango
"""

import random
import pygame
import natrix

options = natrix.options[2]


class Igra(natrix.predmet.PredmetSprite):
    def __init__(self, topleft=(200, 200)):
        natrix.predmet.PredmetSprite.__init__(self,
                                              natrix.sprites['test_3'],
                                              topleft)

        self.image_index = 0
        self.ribe = []
        self.broji = []
        self.broj = 0

        #  generiranje i pozicioniranje slova na ekran
        for i in range(4):
            self.broji.append(Broj([1350, 230*i], 0, self))

        for i in self.broji:
            natrix.group_sprite.add(i)

        self.gen()

    def gen(self):
        for r in self.ribe:
            natrix.group_sprite.remove(r)

        self.ribe = []

        svi = random.sample(list(range(1, 11)), 4)

        self.broj = random.choice(svi)

        mesta = random.sample(list(range(20)), k=self.broj)
        print(mesta)

        stan = [[0, 1, 7], [0, 1, 7], [0, 1, 7], [0, 1, 7], [0, 1, 7],
                [0, 1, 2, 4], [0, 1, 7], [0, 1, 7], [0, 1, 7], [0, 1, 7],
                [2, 4], [5, 6, 8], [2, 4], [5, 6, 8], [2, 4, 7],
                [5, 6, 8], [5, 6, 8], [3, 5, 6, 8], [3, 5, 6, 8], [3, 5, 6, 8]]

        for m in mesta:
            x = 50 + (m % 5)*260 + random.randint(-30, 30)
            y = 30 + (m // 5)*215 + random.randint(-30, 30)

            image_index = random.choice(stan[m])

            self.ribe.append(Riba((x, y), image_index))

        for i in self.ribe:
            natrix.group_sprite.add(i)


        for i, br in enumerate(svi):
            self.broji[i].image_index = br



class Broj(natrix.predmet.PredmetSprite):
    def __init__(self, topleft=(200, 200), image_index=0, parent=None):
        natrix.predmet.PredmetSprite.__init__(self,
                                              natrix.sprites['test_3'],
                                              topleft)

        self.parent = parent
        self.image_index = image_index
#
    def lmb_down(self):
        if self.image_index == self.parent.broj:
            natrix.kond.stop()
            natrix.kanal.play(natrix.sounds['62'])
            self.parent.gen()
        else:
            natrix.kond.stop()
            natrix.kanal.play(natrix.sounds['60'])


class Riba(natrix.predmet.PredmetSprite):
    def __init__(self, topleft=(200, 200), image_index=0):
        natrix.predmet.PredmetSprite.__init__(self,
                                              natrix.sprites['ribe'],
                                              topleft)

        self.image_index = image_index



natrix.rooms['room_2'].clsarg.append((Igra, {'topleft': (-150, -150)}))
