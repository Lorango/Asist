# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 14:45:47 2017
Samo test da vidin kako funkcionira gutgab i source tree-
@author: Lorango
"""
import random
import pygame
import natrix

natrix.load_image('grafics/novaslova.png')

sprite_1 = natrix.Sprite('test3', 'grafics/novaslova.png',
                         (0, 0, 100, 100), 6)


class Igra(natrix.predmet.PredmetSprite):
    def __init__(self, topleft=(200, 200)):
        natrix.predmet.PredmetSprite.__init__(self, sprite_1, topleft)

        self.image_index = 0
        self.slova = []  # objekti koji se stišće
        #  generiranje i pozicioniranje slova na ekran
        for i in range(5):
            self.slova.append(Slovo(0, (100 + 130*(i % 5), 200)))

        for i in self.slova:
            natrix.group_sprite.add(i)

        self.gen()

    def step(self):
        pass

    def gen(self):
        """Popunjavanje i odabir slova ke će se pojavit na ekran.

        """
        self.ras = [0, 99]  # raspon slova
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
    def __init__(self, i=0, topleft=(200, 200)):
        natrix.predmet.PredmetSprite.__init__(self, sprite_1, topleft)
        self.timer = 0
        self.image_index = i

    def lmb_down(self):
        if self.image_index == igra.image_index:
            print('Točno')
            igra.gen()
        else:
            print('Krivo')

igra = Igra((350, 30))
natrix.group_sprite.add(igra)
