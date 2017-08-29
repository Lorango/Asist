# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 14:42:16 2017

@author: Lorango
"""

import pygame
import natrix.tools


class Primitive(pygame.sprite.Sprite):
    def __init__(self, rect=(0, 0, 80, 80), image=None, layer=300):
        pygame.sprite.Sprite.__init__(self)

        self.rect = pygame.Rect(rect)
        self.rect_org = self.rect.copy()

        self.image = pygame.Surface(self.rect.size)
        self.image.fill(natrix.tools.gray)

        self._layer = layer

        natrix.tools.Controler.event_group.add(self)

    def draw(self, surface):
        return surface.blit(self.image, self.rect.topleft)

    def lmb_down(self):
        print('Go')
        pass

    def lmb_up(self):
        pass


class Grupa:
    def __init__(self):
        self.sprites_list = []
        pass

    def __iter__(self):
        return iter(self.sprites_list)

    def add(self, sprite):
        self.sprites_list.append(sprite)
        pass

    def remove(self):
        # WIP
        pass

    def empty(self):
        self.sprites_list = []
        pass

    def draw(self, surface):
        for i in self.sprites_list:
            x, y = i.rect.topleft
            x -= natrix.tools.Controler.camera.rect.left
            y -= natrix.tools.Controler.camera.rect.top
            surface.blit(i.image, (x, y))
