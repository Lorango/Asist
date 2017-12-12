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
rez_def = (800, 480) # izvorna rezolucija pri kojoj je igra razvijena
rez = (800, 480) # rezolucija prikaza
rez = (1920, 1080) # rezolucija prikaza
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


def load_image(path='data/images/cat.png'):
    """Docstring

    """
    if path not in images.keys():
        surface = pygame.image.load(path).convert_alpha()
        surface = pygame.transform.scale(surface, natrix.scale(surface.get_size())) # skaliranje zo rastezanjen.
#        surface = pygame.transform.scale(surface, (round(surface.get_width()*min(scale_f)), (round(surface.get_height()*min(scale_f))))) # nespretno napisano napravit funkciju za skaliranje koja će moć to lipše odradit.
        images[path] = surface
        return surface


class Sprite:
    """Docstring
    Sadrži podatke kako blitat sprite sa slike na ekran.

    """
    def __init__(self, sprite_name, image_name='data/images/brendan.png',
                 rect=(0, 0, 14, 21), n=3):

        self.name = sprite_name
        self.image_name = image_name
        self.rect = pygame.Rect(rect)

        print(self.rect, type(self.rect.size))
        self.rect.inflate_ip(self.rect.w*(scale_f[0] - 1), self.rect.h*(scale_f[1] - 1))
        self.rect.topleft = (0, 0)
        print(self.rect, type(self.rect.size))

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
#        print(jkl)
#        jkl = (round(min(natrix.scale_f)*(dim[0] // self.rect.width)), round(min(natrix.scale_f)*(dim[1] // self.rect.height)))
#        print(jkl)
        x = self.rect.width*(i % jkl[0])
        y = self.rect.height*(i // jkl[0])
        screen.blit(images[self.image_name], topleft,
                    self.rect.move(x, y))
        pass

def goto_room(room_name='room_0'):
    room = rooms[room_name]
    room.stop()
    room.start()
    pass
