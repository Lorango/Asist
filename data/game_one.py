# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 13:53:13 2017

@author: Lorango
"""

import random
import natrix


options = natrix.options[1]


class Igra(natrix.predmet.PredmetSprite):
    def __init__(self, topleft=(200, 200)):
        natrix.predmet.PredmetSprite.__init__(self,
                                              natrix.sprites['test_3'],
                                              topleft)

        global options
        options = natrix.options[1]

        self.image_index = 0
        self.slova = []  # objekti koji se stišće

        #  generiranje i pozicioniranje slova na ekran
        self.n_ = int(options[0].text)  # broj izbora rješenja

        # width - skalirana žirina sličice bez utjecaja skaliranja rezolucije
        width = natrix.sprites['test_3'].wh[0] / natrix.scale_f[0]

        # delta - pomak između pojedinih izbora
        delta = (natrix.rez_def[0] - width*self.n_)/(self.n_+1)

        # 2*offset; offset - odmak od od ruba ekrana
        offset = natrix.rez_def[0] - (width*self.n_ + delta*(self.n_ - 1))
        offset //= 2

        for i in range(self.n_):
            self.slova.append(Slovo(0, (offset + i*(width+delta), 350), self))

        for i in self.slova:
            natrix.group_sprite.add(i)

        self.gen()

    def step(self):
        pass

    def gen(self):
        """Popunjavanje i odabir slova ke će se pojavit na ekran.

        """
        self.ras = []  # sadrži sve indekse ke se more odabrat
        eng = int(options[5].text)  # uključi engleske znakove
        if int(options[1].text):
            self.ras.extend(list(range(10)))

        if int(options[2].text):
            self.ras.extend(list(range(10, 20)))

        if int(options[3].text):
            self.ras.extend(list(range(20, 50 + 4*eng)))

        if int(options[4].text):
            self.ras.extend(list(range(60, 90 + 4*eng)))

        self.indeksi = random.sample(self.ras, self.n_)  # odabir kandidata
        self.image_index = random.choice(self.indeksi)  # odabir traženoga

        # svakom slovu postavi njegov index
        for i, slovo in enumerate(self.slova):
            slovo.image_index = self.indeksi[i]

        # pozovi sintezu govora
        natrix.kond.generator(self.image_index)


class Slovo(natrix.predmet.PredmetSprite):
    def __init__(self, i=0, topleft=(200, 200), parent=None):
        natrix.predmet.PredmetSprite.__init__(self,
                                              natrix.sprites['test_3'],
                                              topleft)
        self.parent = parent
        self.image_index = i

    def lmb_down(self):
        if self.image_index == self.parent.image_index:
            natrix.kond.stop()
            natrix.kanal.play(natrix.sounds['62'])
            self.parent.gen()
        else:
            natrix.kond.stop()
            natrix.kanal.play(natrix.sounds['64'])


natrix.rooms['room_1'].clsarg.append((Igra, {'topleft': (-450, 0)}))
