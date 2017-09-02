# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 14:41:17 2017

@author: Lorango

Natrix je modul ki je nadogradnja funkcionalnosti pygame-a i osmišljen je kao
game engine koji objedinjuje igru, pygame i Tiled editor (.tmx i .tsx)
Modul sadrši funkcionalnosti za stvaranje soba, kamera i slično.
"""

import pygame
import natrix.tools
import natrix.sprite
import natrix.gui

pygame.font.init()
font_def = pygame.font.Font(None, 50)

print('Test za vidit koliko puti će se učitat natrix modul.')


black = pygame.Color(0, 0, 0)
gray = pygame.Color(110, 110, 110)
white = pygame.Color(255, 255, 255)

red = pygame.Color(255, 0, 0)
orange = pygame.Color(255, 110, 0)
yellow = pygame.Color(255, 255, 0)
lime = pygame.Color(110, 255, 0)
green = pygame.Color(0, 255, 0)
greenblue = pygame.Color(0, 255, 110)
cyan = pygame.Color(0, 255, 255)
indigo = pygame.Color(0, 110, 255)
blue = pygame.Color(0, 0, 255)
purple = pygame.Color(110, 0, 255)
magenta = pygame.Color(255, 0, 255)
pink = pygame.Color(255, 0, 110)


class Controller():
    """Docstring

    """
    screen = pygame.display.set_mode((800, 480))
    clock = pygame.time.Clock()

    camera = natrix.tools.Camera()
#    group = natrix.sprite.Group()
    group = natrix.sprite.GroupCamera()
    group_gui = natrix.sprite.Group()

    @classmethod
    def step(cls):
        """Docstring

        """
        for sprite in cls.group:
            sprite.step()

        for sprite in cls.group_gui:
            sprite.step()

    @classmethod
    def draw(cls):
        """Docstring

        """
        cls.screen.fill(yellow)
        cls.camera.update()
        cls.group.draw(cls.screen)
        cls.group_gui.draw(cls.screen)

    @classmethod
    def go_to_room(cls, name):
        """Docstring

        """
        #  go tu grup
        cls.room_active = cls.rooms[name]

        # isprazni event_group
        for sprite in cls.event_group:
            cls.event_group.remove()

        cls.room_active.load()
        cls.event_group.add(cls.room_active.objekti)
