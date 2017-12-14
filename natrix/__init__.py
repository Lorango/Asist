# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 14:41:17 2017

@author: Lorango

Natrix je modul ki je nadogradnja funkcionalnosti pygame-a i osmišljen je kao
game engine koji objedinjuje igru, pygame i Tiled editor (.tmx i .tsx)
Modul sadrši funkcionalnosti za stvaranje soba, kamera i slično.
"""

import math
import pygame
import natrix.tools
import natrix.predmet
import natrix.gui


pygame.font.init()
font_def = pygame.font.Font(None, 50)

print('Test za vidit koliko puti će se učitat natrix modul.')

#  Boje
black = pygame.Color(0, 0, 0)
gray = pygame.Color(200, 200, 200)
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
# rezolucije "eksperiment!"
rez_def = (1920, 1080) # izvorna rezolucija pri kojoj je igra razvijena
#rez = (800, 480) # rezolucija prikaza
rez = (1000, 600) # rezolucija prikaza
#rez = (1020, 1020) # rezolucija prikaza
scale_f = (rez[0]/rez_def[0], rez[1]/rez_def[1]) #faktor skaliranja

screen = pygame.display.set_mode(rez)
clock = pygame.time.Clock()

images = {}
sprites = {}
rooms = {}

camera = natrix.tools.Camera()

#group = natrix.predmet.GroupCamera()
group_sprite = natrix.predmet.GroupCameraSprite()
#group_gui = natrix.predmet.Group()


rooms['room_0'] = natrix.tools.Room()
#room = rooms['room_0']


#room_1 = natrix.tools.Room()
#rooms['room_0'] = room_1

def scale(topleft):
    """Skaliranje koordinata.
    Prima polje koordinata (x, y), duljine 2. [topleft]
    Vraća skalirane koordinate (x', y'). [_topleft]

    """
    _topleft = []
    for x, s in zip(topleft, scale_f):
        _topleft.append(round(x*s))

#    print(_topleft)

    return _topleft


def step():
    """Docstring

    """
#    for predmet in group:
#        predmet.step()

    for predmet in group_sprite:
        predmet._step()

#    for predmet in group_gui:
#        predmet.step()


def draw():
    """Docstring

    """
    screen.fill(white)
    camera.update()
#    group.draw(screen)
    group_sprite.draw()
#    group_gui.draw(screen)


def load_image(path='data/images/cat.png', size=[10, 10]):
    """Docstring

    """
#    screen.fill(white)
    if path not in images.keys():
        surface = pygame.image.load(path).convert_alpha()

        image_size = surface.get_size()
        a = round(image_size[0]/size[0])
        b = round(image_size[1]/size[1])

        c, d = natrix.scale((a, b))

        print(a, b)
        print(c, d)

        surface_ = pygame.Surface((c * size[0], d * size[1])).convert_alpha()
        surface_.fill((0, 255, 255, 0))
        print(surface_)

        kalup = pygame.Surface((a, b)).convert_alpha()
        kalup.fill((0, 255, 255, 0))

        for j in range(size[0]):  # broj redova
            y = b*j
            for i in range(size[1]):  # broj stupaca
                x = a*i
                temp = kalup.copy()
                temp.blit(surface, (0, 0), (x, y, a, b))
                temp = pygame.transform.smoothscale(temp, natrix.scale((a, b)))
                screen.blit(temp, (x, y), (0, 0, c, d))
                surface_.blit(temp, (c*i, d*j), (0, 0, c, d))
                pass

        images[path] = surface_
        return surface_


class Sprite:
    """Docstring
    Sadrži podatke kako blitat sprite sa slike na ekran.

    """
    def __init__(self, sprite_name, image_name='data/images/brendan.png',
                 size=[10, 10]):

        self.name = sprite_name
        self.image_name = image_name
        self.size = size
        self.subimages = []
        self.speed = 30  # Broj potrebnih frame-ova za promjenu sličice.

        self.calc()

    def calc(self):
        image_size = images[self.image_name].get_size()
        a = image_size[0]/self.size[0]
        b = image_size[1]/self.size[1]

        y_pred = -b
        for j in range(self.size[0]):  # broj redova
            x_pred = -a
            y = b*j
            h = y - y_pred
            y_pred = y
            for i in range(self.size[1]):  # broj stupaca
                x = a*i
                w = x - x_pred
                x_pred = x

                self.subimages.append(pygame.Rect(round(x), round(y),
                                                  round(w), round(h)))


    def draw(self, topleft, i):
        """Docstring
        Blita direktno sa slike na ekran.

        """
        screen.blit(images[self.image_name], topleft, self.subimages[i])
        pass


def goto_room(room_name='room_0'):
    room = rooms[room_name]
    room.stop()
    room.start()
    pass
