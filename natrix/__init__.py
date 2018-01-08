# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 14:41:17 2017

@author: Lorango

Natrix je modul ki je nadogradnja funkcionalnosti pygame-a i osmišljen je kao
game engine koji objedinjuje igru, pygame i Tiled editor (.tmx i .tsx)
Modul sadrši funkcionalnosti za stvaranje soba, kamera i slično.
"""

import math
import xml.etree.ElementTree as ET
import pygame
import natrix.tools
import natrix.predmet
import natrix.gui

import data.sinteza as snt

tree = ET.parse('options.txt')
options = tree.getroot()

pygame.font.init()
pygame.mixer.init(frequency=48000)
#pygame.mixer.init(frequency=70000)
kanal = pygame.mixer.Channel(0)
kanal.set_endevent(25)
kond = snt.Kond()


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

neutral_c = pygame.Color(19, 25, 38)  # neutralno črno siva boja

#  Kontrolne varijable
rez_def = (1600, 900)  # izvorna rezolucija pri kojoj je igra razvijena
#rez = (1600, 900)
#rez = (1920, 1080)
#rez = (800, 450)  # rezolucija prikaza
rez = (int(options[0][0][0].text), int(options[0][0][1].text))
scale_f = (rez[0]/rez_def[0], rez[1]/rez_def[1])  # faktor skaliranja

full_screen = False
screen = pygame.display.set_mode(rez)
clock = pygame.time.Clock()

images = {}
static_images = {}
sprites = {}
sounds = {}
rooms = {}

camera = natrix.tools.Camera()

#group = natrix.predmet.GroupCamera()
group_sprite = natrix.predmet.GroupCameraSprite()
#group_gui = natrix.predmet.Group()

rooms['room_0'] = natrix.tools.Room()

room_t = 'room_0' # trenutna soba

def scale(topleft, relative_size=1, rs=0):
    """Skaliranje koordinata.
    Prima polje koordinata (x, y), duljine 2. [topleft]
    Vraća skalirane koordinate (x', y'). [_topleft]

    """
    _topleft = []
    for x, s in zip(topleft, scale_f):
        if rs:
            size = round(x*s*relative_size)
        else:
            size = round(x*s)
        _topleft.append(size)

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
    screen.fill(neutral_c)

    image_name = rooms[room_t].static_image
    if image_name is not None:
        screen.blit(static_images[image_name].surface, (0,0))

    camera.update()
#    group.draw(screen)
    group_sprite.draw()
#    group_gui.draw(screen)


class Sprite:
    """Docstring
    Sadrži podatke kako blitat sprite sa slike na ekran.

    """
    def __init__(self, sprite_name, image_path='data/images/brendan.png',
                 size=[10, 10], relative_size = 1):

        # size = [broj redova, broj stupaca]

        self.name = sprite_name
        self.image_path = image_path
        self.size = size
        self.subimages = []
        self.speed = 30  # Broj potrebnih frame-ova za promjenu sličice.

        self.wh = [100, 100]  # skalirana širina i visina podsličice
        self.relative_size = relative_size

        self.load_image(image_path, size)

        sprites[sprite_name] = self

    def draw(self, topleft, i):
        """Docstring
        Blita direktno sa slike na ekran.

        """
        screen.blit(images[self.image_path][0], topleft, self.subimages[i])
        pass

    def load_image(self, image_path, size):
        """Učitava sliku, skalira je i određuje skalirane odsječke
        za sprite-ove.

        Rabi predelat na način da omogućava kreiranje drugoga sprite-a sa iste
        slike.
        """
        if image_path not in images.keys():
            surface = pygame.image.load(image_path).convert_alpha()
            image_size = surface.get_size()
            w = round(image_size[1]/size[0])  # širina podsličice
            h = round(image_size[0]/size[1])

            # skalirana širina i visina podsličice
            w_, h_ = natrix.scale((w, h), self.relative_size, 1)
#            self.wh = [w_, h_]
            self.wh = [w_, h_]
            surface_ = pygame.Surface((w_ * size[1],
                                       h_ * size[0])).convert_alpha()

            surface_.fill((0, 255, 255, 0))
            kalup = pygame.Surface((w, h)).convert_alpha()
            kalup.fill((0, 255, 255, 0))
            for j in range(size[0]):  # broj redova
                y = h*j
                y_ = h_*j
                for i in range(size[1]):  # broj stupaca
                    x = w*i
                    x_ = w_*i
                    temp = kalup.copy()
                    temp.blit(surface, (0, 0), (x, y, w, h))
                    temp = pygame.transform.smoothscale(temp, (w_, h_))
                    rect = surface_.blit(temp, (x_, y_), (0, 0, w_, h_))
                    self.subimages.append(rect)

            meta_data = (size, (w_, h_))
            images[image_path] = (surface_, meta_data)
        else:
            """Za implementirat u budućnosti. Vjerovatno će zahtjevat
            rekonstrukciju algoritma učitavanja i skaliranja.

            """
            pass


def goto_room(room_name='room_0'):
    global room_t
    room = rooms[room_name]
    room.stop()
    room.start()
    room_t = room_name
    pass


class Static_image():
    def __init__(self, sprite_name, image_path='', relative_size=1, stretch=[1, 1]):

        print('sadfasdf dsjf jsdfa lsdajfh')

        self.name = sprite_name
        self.surface = None
        self.relative_size = relative_size
        self.stretch = stretch

        self.load_image(image_path)
        self.resize(stretch)

        static_images[sprite_name] = self
        pass

    def load_image(self, image_path):
        self.surface = pygame.image.load(image_path).convert_alpha()

    def resize(self, stretch):
        size = self.surface.get_size()

        new_size = []
        for s, res, raz in zip(size, scale_f, stretch):
            a = math.ceil(s * res * raz)
            new_size.append(a)

        print(new_size)
        self.surface = pygame.transform.smoothscale(self.surface, new_size)

#        pygame.Surface(new_size)

        pass


















