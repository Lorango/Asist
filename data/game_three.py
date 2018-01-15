# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 13:53:53 2017

@author: Lorango
"""


import random
import natrix

options = natrix.options[3]

class Igra(natrix.predmet.PredmetSprite):
    def __init__(self, topleft=(200, 200)):
        natrix.predmet.PredmetSprite.__init__(self,
                                              natrix.sprites['slike'],
                                              topleft)

        global options
        options = natrix.options[3]

        self.image_index = 0
        self.slova = []  # objekti koji se stišće
        #  generiranje i pozicioniranje slova na ekran
        self.n_ = int(options[0].text)  # broj izbora rješenja

        # width - skalirana žirina sličice bez utjecaja skaliranja rezolucije
        width = natrix.sprites['slike'].wh[0] / natrix.scale_f[0]

        # delta - pomak između pojedinih izbora
        delta = (natrix.rez_def[0] - width*self.n_)/(self.n_+1)

        # 2*offset; offset - odmak od od ruba ekrana
        offset = natrix.rez_def[0] - (width * self.n_ + delta * (self.n_ - 1))
        offset //= 2

        for i in range(self.n_):
            self.slova.append(Slovo(0, (offset + i*(width+delta), 350), self))

        for i in self.slova:
            natrix.group_sprite.add(i)

        self.pomoc = Pomoc((710, 30 - 500 + 500*int(options[9].text)), natrix.sprites['test_3'])
        natrix.group_sprite.add(self.pomoc)

        self.gen()

    def step(self):
        pass

    def gen(self):
        """Popunjavanje i odabir slova ke će se pojavit na ekran.

        """
        br_sl = 5 # broj sličica u sprite Sheetu.
#        black_set = {x for x in range(150) if (x % br_sl) > 2}
#        black_set |= {42, 45, 61, 62, 96, 97, 131, 132, 147}
        black_set = {23, 24, 35, 37, 38, 39, 44, 63, 64, 84, 96, 97, 98, 99}

        # generiranje pune liste setova indeksa
        full_list = []
        for i in range(30):
            set_ = {i*br_sl + x for x in range(br_sl)}
            full_list.append(set_)

#        print(full_list, '\n')

        # izbacivanje indeksa koji se nekoriste iz setova.
        for i, set_ in enumerate(full_list):
            full_list[i] -= black_set

#        print(full_list, '\n')

        # pod set
        g_sub = [[0, 8, 12, 20, 26],
                 [1, 2, 3, 4, 5],
                 [6, 7, 9, 10, 11],
                 [13, 14, 15, 26, 17],
                 [18, 19, 21, 22, 23],
                 [24, 25, 27, 28, 29]]

        # odabir podseta
        sub_list = []
        for i in range(6):
            if int(options[i + 1].text):
                sub_list += g_sub[i]
#        print(sub_list, '\n')

        # odabir traženoga
        self.image_index = random.choice(sub_list)
        self.pomoc.image_index = self.image_index + 20# služi za pomoć

        natrix.kond.generator_3(self.image_index)  # generiraj listu za izgovor

        # odabir seta izbor slova
        izbor_ = [self.image_index]


        # broj izbora rješenja - 1
        n_izb = int(options[0].text) - 1
        duplikati = int(options[8].text)
        if not(int(options[7].text)):
            # izaberi "n_izb" iz skupa koji ne sadrži riješenje
            izbor_lista = list(set(range(30)) - set(izbor_))
            if duplikati:
                izbor_ += random.choices(izbor_lista, k=n_izb)
            else:
                izbor_ += random.sample(izbor_lista, n_izb)
        else:
            izbor_lista = list(set(sub_list) - set(izbor_))
            if duplikati:
                izbor_ += random.choices(izbor_lista, k=n_izb)
            else:
                izbor_ += random.sample(izbor_lista, n_izb)

#        print(izbor_, '\n')

        # odabir varijacija sličica
        for i, data in enumerate(izbor_):
            izbor_[i] = random.sample(full_list[data], 1)[0]

        self.image_index = izbor_[0]

        random.shuffle(izbor_)

#        print(izbor_, '\n')

        # svakom slovu postavi njegov index
        for i, slovo in enumerate(self.slova):
            slovo.image_index = izbor_[i]


class Slovo(natrix.predmet.PredmetSprite):
    def __init__(self, i=0, topleft=(200, 200), parent=None):
        natrix.predmet.PredmetSprite.__init__(self,
                                              natrix.sprites['slike'],
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
            natrix.kanal.play(natrix.sounds['60'])
            pass

class Pomoc(natrix.predmet.PredmetSprite):
    def __init__(self, topleft=(200, 200), sprite=None, image_index=0):
        natrix.predmet.PredmetSprite.__init__(self, sprite, topleft)

        self.image_index = image_index

natrix.rooms['room_3'].clsarg.append((Igra, {'topleft': (-450, 0)}))
