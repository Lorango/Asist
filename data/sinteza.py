# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 14:18:47 2018

@author: Lorango

Sadrži funkcije korištene za reprodukciju zvuka
"""

from collections import deque
import natrix


class Kond():
    """(kondukter) Upravlja zo reprodukciju zvučnih kanali.

    """
    def __init__(self):
        self.queue = deque([54, 58, 8])
        pass

    def stop(self):
        self.queue = deque([])

    def update_queue(self):
#        if self.stop:
#            self.queue = deque([])
#            self.stop = False

        if len(self.queue) > 0:
            i = self.queue.popleft()
            natrix.kanal.queue(natrix.sounds[str(i)])
        pass

    def generator(self, index):
        """ds

        """
        self.queue = deque([54])
        if index >= 0 and index <= 19:
            self.queue.append(58)

        elif index >= 20 and index <= 59:
            self.queue.append(56)
            self.queue.append(57)

        elif index >= 60 and index <= 99:
            self.queue.append(55)
            self.queue.append(57)
            index -= 40

        self.queue.append(index)
        self.update_queue()

    def generator_3(self, index):
        """

        """
        self.queue = deque([54, 59])
#        if index >= 0 and index <= 19:
#            self.queue.append(58)
#
#        elif index >= 20 and index <= 59:
#            self.queue.append(56)
#            self.queue.append(57)
#
#        elif index >= 60 and index <= 99:
#            self.queue.append(55)
#            self.queue.append(57)
#            index -= 40
#
#        self.queue.append(index)
        self.update_queue()

    def test(self):
        natrix.kanal.queue(natrix.sounds[str(0)])