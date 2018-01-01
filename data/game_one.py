# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 13:53:13 2017

@author: Lorango
"""

import random
import natrix

options = []


class Igra(natrix.predmet.PredmetSprite):
    def __init__(self, topleft=(200, 200)):
        natrix.predmet.PredmetSprite.__init__(self,
                                              natrix.sprites['test_3'],
                                              topleft)

        self.image_index = 0
        self.slova = []  # objekti koji se stišće

        #  generiranje i pozicioniranje slova na ekran
        self.n_ = int(options[4].text)  # broj izbora rješenja

        # delta - pomak između pojedinih izbora i između ruba ekrana
        delta = (1600-300*self.n_)/(self.n_+1)
        for i in range(self.n_):
            self.slova.append(Slovo(0,
                                    (300*(i % self.n_) + delta*(1 + i), 350),
                                    self))

        for i in self.slova:
            natrix.group_sprite.add(i)

        self.gen()

    def step(self):
        pass

    def gen(self):
        """Popunjavanje i odabir slova ke će se pojavit na ekran.

        """
        self.ras = []  # sadrži sve indekse ke se more odabrat
        eng = int(options[3].text)  # uključi engleske znakove
        if int(options[0].text):
            self.ras.extend(list(range(10 + 1)))

        if int(options[1].text):
            self.ras.extend(list(range(20, 50 + 4*eng)))

        if int(options[2].text):
            self.ras.extend(list(range(60, 90 + 4*eng)))

        self.indeksi = random.sample(self.ras, self.n_)  # odabir kandidata
        self.image_index = random.choice(self.indeksi)  # odabir traženoga

        # svakom slovu postavi njegov index
        for i, slovo in enumerate(self.slova):
            slovo.image_index = self.indeksi[i]


class Slovo(natrix.predmet.PredmetSprite):
    def __init__(self, i=0, topleft=(200, 200), parent=None):
        natrix.predmet.PredmetSprite.__init__(self,
                                              natrix.sprites['test_3'],
                                              topleft)
        self.parent = parent
        self.image_index = i

    def lmb_down(self):
        if self.image_index == self.parent.image_index:
            print('Točno')
            self.parent.gen()
        else:
            print('Krivo', self.rect)


natrix.rooms['room_1'].clsarg.append((Igra, {'topleft': (400, 0)}))