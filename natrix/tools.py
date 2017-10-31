# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 15:01:37 2017

@author: Lorango
"""

import pygame

#import tmx


def foo():
    print('Foo bar spam.')


def tilemap_create(path='maps/otok_2.tmx'):
    mapa = tmx.TileMap.load(path)
    obj = []
    tileset = pygame.image.load('maps/terrain_3.png')
    tilemap = pygame.Surface((mapa.width*mapa.tilewidth,
                              mapa.height*mapa.tileheight))

    for layer in mapa.layers:
        if type(layer) == tmx.Layer:
            for i, tile in enumerate(layer.tiles):
                # sprječava nepotrebna blitanja pratnih tilova.
                if tile.gid == 0:
                    continue

                map_x = (i % mapa.width)*32
                map_y = (i//mapa.width)*32
                tileset_x = ((tile.gid-1) % 32)*32
                tileset_y = ((tile.gid-1)//32)*32
                tilemap.blit(tileset, (map_x, map_y),
                             (tileset_x, tileset_y, 32, 32))

        elif type(layer) == tmx.ObjectGroup:
            for objekt in layer.objects:
                svojstva = {}
                for svojstvo in objekt.properties:
                    svojstva[svojstvo.name] = \
                        Controler.funkcije[svojstvo.value]

#                    print(svojstvo.name, svojstvo.value)

                svojstva['rect'] = pygame.Rect(objekt.x, objekt.y,
                                               objekt.width, objekt.height)

                obj.append(Controler.klase[objekt.type](**svojstva))

    return tilemap, obj


class Room():
    def __init__(self, path='maps/otok_2.tmx'):
        self.path = path
        self.persistent = False
        self.mapa = None
        self.objekti = None

        name = self.path.split('/')[-1].split('.')[0]
        Controler.rooms[name] = self
        print(self.path)

    def load(self):
        self.mapa, self.objekti = tilemap_create(self.path)


class Camera():
    """Docstring

    mode = 0
    Kamera isključena

    mode = 1
    Kamera prati miš

    mode = 2
    Kamera instancu klase (predmet)

    """
    def __init__(self, mode = 0):
        self.rect = pygame.Rect(0, 0, 800, 480)
        self.mode = mode
        self.predmet = None

    def update(self):
        """Docstring

        """
        if self.mode == 1:
            self.rect.center = pygame.mouse.get_pos()
        elif self.mode == 2 and self.predmet is not None:
            self.rect.center = self.predmet.rect.center
