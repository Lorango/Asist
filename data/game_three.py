# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 13:53:53 2017

@author: Lorango
"""


import random
import natrix

options = []


class Igra(natrix.predmet.PredmetSprite):
    def __init__(self, topleft=(200, 200)):
        natrix.predmet.PredmetSprite.__init__(self,
                                              natrix.sprites['slike'],
                                              topleft)

        self.image_index = 0
        self.slova = []  # objekti koji se stišće
        #  generiranje i pozicioniranje slova na ekran
        self.n_ = int(options[0].text)  # broj izbora rješenja

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
        # automatsko filtriranje
        black = {x for x in range(150) if (x % 5) > 2}
        # rucno filtriranje
        black |= {42, 45, 61, 62, 95, 96, 97, 130, 131, 132, 147}

        self.ras = set(range(150)) - black

        self.indeksi = random.sample(self.ras, self.n_)  # odabir kandidata
        self.image_index = random.choice(self.indeksi)  # odabir traženoga

        # svakom slovu postavi njegov index
        for i, slovo in enumerate(self.slova):
            slovo.image_index = self.indeksi[i]


class Slovo(natrix.predmet.PredmetSprite):
    def __init__(self, i=0, topleft=(200, 200), parent=None):
        natrix.predmet.PredmetSprite.__init__(self,
                                              natrix.sprites['slike'],
                                              topleft)
        self.parent = parent
        self.image_index = i

    def lmb_down(self):
        if self.image_index == self.parent.image_index:
            print('Točno')
            self.parent.gen()
        else:
            print('Krivo', self.rect)


natrix.rooms['room_3'].clsarg.append((Igra, {'topleft': (400, 0)}))
