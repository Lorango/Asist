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
        black_set = {x for x in range(150) if (x % 5) > 2}
        black_set |= {42, 45, 61, 62, 96, 97, 131, 132, 147}

        # generiranje pune liste setova indeksa
        full_list = []
        for i in range(30):
            set_ = {i*5 + x for x in range(5)}
            full_list.append(set_)

        print(full_list, '\n')

        # izbacivanje indeksa koji se nekoriste iz setova.
        for i, set_ in enumerate(full_list):
            full_list[i] -= black_set

        print(full_list, '\n')

        # # test

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
        print(sub_list, '\n')

        # odabir traženoga
        self.image_index = random.choice(sub_list)
        # odabir seta izbor slova
        izbor_ = [self.image_index]

        if not(int(options[7].text)):
            # izaberi 4 iz skupa koji ne sadrži riješenje
            izbor_ += random.sample(set(range(30)) - set(izbor_), 4)
        else:
            izbor_ += random.sample(set(sub_list) - set(izbor_), 4)

        print(izbor_, '\n')

        # odabir varijacija sličica
        for i, data in enumerate(izbor_):
            izbor_[i] = random.sample(full_list[data], 1)[0]

        self.image_index = izbor_[0]

        random.shuffle(izbor_)

        print(izbor_, '\n')

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
#            print('Točno')
            self.parent.gen()
        else:
#            print('Krivo', self.rect)
            pass


natrix.rooms['room_3'].clsarg.append((Igra, {'topleft': (400, 0)}))
