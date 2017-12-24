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
#        self.ras = [60, 89]  # raspon slova
        self.ras = []
        if int(options[0].text):
            self.ras.extend(list(range(10 + 1)))
            
        if int(options[1].text):
            self.ras.extend(list(range(20 + 1, 50 + 1 + 3 * int(options[3].text))))
            
        if int(options[2].text):
            self.ras.extend(list(range(60 + 1, 90 + 1 + 3 * int(options[3].text))))
            
        self.image_index = random.choice(self.ras)
        self.indeksi = [self.image_index]  # sliži za odabir slova
        for i in range(4):
            r = random.choice(self.ras)
            while r in self.indeksi:
                r = random.choice(self.ras)

            self.indeksi.append(r)

        random.shuffle(self.indeksi)

        for i in range(5):
            self.slova[i].image_index = self.indeksi[i]


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
