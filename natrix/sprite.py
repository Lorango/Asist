# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 14:42:16 2017

@author: Lorango
"""

import pygame
import natrix


class Primitive():
    """Docstring

    """
    def __init__(self, rect=(0, 0, 80, 80), image=None):
        self.rect = pygame.Rect(rect)
        if image is None:
            self.image = pygame.Surface(self.rect.size)
            self.image.fill(natrix.gray)
        else:
            self.image = image
            self.rect.size = self.image.get_rect().size

    def step(self):
        """Docstring

        """
        pass

    def lmb_down(self):
        """Docstring

        """
        pass

    def lmb_up(self):
        """Docstring

        """
        pass


class Sprite(Primitive):
    """Docstring

    """
    def __init__(self, rect, image):
        Primitive.__init__(self, rect, image)

        self.groups = []

    def __repr__(self):
        """Docstring

        """
        return '<{} sprite(in {} groups)>'.format(self.__class__.__name__,
                                                  len(self.groups))


class Group:
    """Docstring

    """
    def __init__(self):
        self.sprites = []
        pass

    def __iter__(self):
        """Docstring

        """
        return iter(self.sprites)

    def __len__(self):
        """return number of sprites in group

        Group.len(group): return int

        Returns the number of sprites contained in the group.

        """
        return len(self.sprites)

    def __repr__(self):
        """Docstring

        """
        return '<{}({} sprites)>'.format(self.__class__.__name__, len(self))

    def add(self, sprite):
        """Docstring

        """
        if sprite not in self.sprites:
            self.sprites.append(sprite)

        if self not in sprite.groups:
            sprite.groups.append(self)

    def remove(self):
        """Docstring

        """
        # WIP
        pass

    def empty(self):
        """Docstring

        """
        self.sprites = []
        pass

    def draw(self, surface):
        """Docstring

        """
        for i in self.sprites:
            x, y = i.rect.topleft
            surface.blit(i.image, (x, y))


class GroupCamera(Group):
    """Docstring

    """
    def __init__(self):
        Group.__init__(self)

    def draw(self, surface):
        """Docstring

        """
        for i in self.sprites:
            x, y = i.rect.topleft
            x -= natrix.camera.rect.left
            y -= natrix.camera.rect.top
            surface.blit(i.image, (x, y))
