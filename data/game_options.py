# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 16:31:46 2018

@author: Lorango
"""

import natrix


class Butn_rez(natrix.predmet.PredmetSprite):
    def __init__(self, i=0, topleft=(200, 200), parent=None):
        natrix.predmet.PredmetSprite.__init__(self,
                                              natrix.sprites['test_3'],
                                              topleft)
        self.parent = parent
        self.image_index = i

    def lmb_down(self):
        if self.parent.image_index != 100:
            print('Točno')
        else:
            print('Krivo')
