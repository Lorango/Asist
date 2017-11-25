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
import natrix.predmet
import natrix.gui


pygame.font.init()
font_def = pygame.font.Font(None, 50)

print('Test za vidit koliko puti će se učitat natrix modul.')

#  Boje
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

#  Kontrolne varijable
screen = pygame.display.set_mode((800, 480))
clock = pygame.time.Clock()

images = {}
sprites = {}

camera = natrix.tools.Camera()

group = natrix.predmet.GroupCamera()
group_sprite = natrix.predmet.GroupCameraSprite()
group_gui = natrix.predmet.Group()


def step():
    """Docstring

    """
    for predmet in group:
        predmet.step()

    for predmet in group_sprite:
        predmet._step()

    for predmet in group_gui:
        predmet.step()


def draw():
    """Docstring

    """
    screen.fill(yellow)
    camera.update()
    group.draw(screen)
    group_sprite.draw()
    group_gui.draw(screen)


def load_image(path='data/images/cat.png'):
    """Docstring

    """
    if path not in images.keys():
        surface = pygame.image.load(path).convert_alpha()
        images[path] = surface
        return images[path]


class Sprite:
    """Docstring
    Sadrži podatke kako blitat sprite sa slike na ekran.

    """
    def __init__(self, sprite_name, image_name='data/images/brendan.png',
                 rect=(0, 0, 14, 21), n=3):

        self.name = sprite_name
        self.image_name = image_name
        self.rect = pygame.Rect(rect)
        self.subimages = n
        self.speed = 30  # Broj potrebnih frame-ova za promjenu sličice.

    def draw(self, topleft, i):
        """Docstring
        Blita direktno sa slike na ekran.

        """
#        screen.blit(images[self.image_name], topleft,
#                    self.rect.move(self.rect.width*i, 0))

        dim = images[self.image_name].get_size()
        jkl = (dim[0] // self.rect.width, dim[1] // self.rect.height)
        x = self.rect.width*(i % jkl[0])
        y = self.rect.height*(i // jkl[0])
        screen.blit(images[self.image_name], topleft,
                    self.rect.move(x, y))
        pass
