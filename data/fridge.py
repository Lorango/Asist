# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 14:45:47 2017

@author: Lorango
"""

import xml.etree.ElementTree as ET
import pygame
import natrix

sprite_1 = natrix.Sprite('test_3', 'grafics/slova4.png', (10, 10), 0.60)
sprite_2 = natrix.Sprite('slike', 'grafics/slike2.png', (30, 5), 0.60)
sprite_3 = natrix.Sprite('ribe', 'grafics/ribe.png', (3, 3), 0.60)

natrix.Sprite('ikone', 'grafics/buttons.png', (3, 3), 0.40)
natrix.Sprite('buttons', 'grafics/button_slova.png', (6, 4))
natrix.Sprite('rez', 'grafics/button_rez.png', (4, 4), 0.8)
natrix.Sprite('opis', 'grafics/opis.png', (7, 3), 0.7)

static_image_0 = natrix.Static_image('more', 'grafics/podmorje.png', 1, (0.986436498, 1.125))
natrix.Static_image('plain', 'grafics/pozadina.jpg', 1, (1.00, 1.00))
natrix.Static_image('noc', 'grafics/noc.jpg', 1, (1.00, 1.00))
natrix.Static_image('option', 'grafics/option.jpg', 1, (1.00, 1.00))

# učitavanje zvukova
for i in range(64):
    file_name = 'sound/{}.ogg'.format(i)
    natrix.sounds[str(i)] = pygame.mixer.Sound(file_name)



class Goi(natrix.predmet.PredmetSprite):
    def __init__(self, topleft=(200, 200), room_name='room_0',
                 sprite=natrix.sprites['test_3'], image_index=0):
        natrix.predmet.PredmetSprite.__init__(self, sprite, topleft)

        self.room_name = room_name
        self.image_index = image_index
        natrix.group_sprite.add(self)

    def lmb_down(self):
        natrix.kond.stop()
        natrix.goto_room(self.room_name)


class Btn_popravi(Goi):
    """provjeri ispravnost opcija

    """
    def __init__(self, topleft=(200, 200), room_name='room_0', sprite=natrix.sprites['test_3'], image_index=0, game=1):
        Goi.__init__(self, topleft, room_name, sprite, image_index)
        self.game = game
        pass

    def lmb_down(self):
        if self.game == 1:
            a = 5
        elif self.game == 2:
            a = 1
        elif self.game == 3:
            a = 7

        fuse = True
        for i in range(1, a):
            fuse = fuse and not(int(natrix.options[self.game][i].text))
#            natrix.options[self.game][self.opcija_id].text = str(int(self.value))
        if fuse == 1:
            natrix.options[self.game][1].text = str(1)
        Goi.lmb_down(self)


class Btn_1(Goi):
    def lmb_down(self):
        natrix.tree.write('options.txt')
        Goi.lmb_down(self)


class Btn_def(Goi):
    def lmb_down(self):
        natrix.tree = ET.parse('data/options.txt')
        natrix.options = natrix.tree.getroot()


class Full_screen(natrix.predmet.PredmetSprite):
    def __init__(self, topleft=(200, 200),
                 sprite=natrix.sprites['ikone'], image_index=0):

        natrix.predmet.PredmetSprite.__init__(self, sprite, topleft)

        self.image_index = 3 + natrix.full_screen
        natrix.group_sprite.add(self)

        self.opis = Opis((-600, 40), natrix.sprites['opis'], 16)
        natrix.group_sprite.add(self.opis)

    def lmb_down(self):
        natrix.full_screen = not(natrix.full_screen)
        if natrix.full_screen:
            try:
                pygame.display.set_mode(natrix.rez, pygame.FULLSCREEN)
                self.opis.rect.topleft = natrix.scale((-600, 40)) # nije nužno u praksi nebitrabalo ničemu služit
            except:
                print('Izabrana rezolucija je veća od trenutne rezulucije prikaza!')
                print('Odabrati manju rezoluciju prikaza!')
                natrix.full_screen = 0
                self.opis.rect.topleft = natrix.scale((950, 40))
        else:
            pygame.display.set_mode(natrix.rez)

        self.image_index = 3 + natrix.full_screen

class Ugasi(natrix.predmet.PredmetSprite):
    def __init__(self, topleft=(200, 200), image_index=0):
        natrix.predmet.PredmetSprite.__init__(self,
                                              natrix.sprites['ikone'], topleft)

        self.image_index = image_index
        natrix.group_sprite.add(self)

    def lmb_down(self):
        pygame.event.post(pygame.event.Event(12, {}))
        if natrix.full_screen:
            pass
        else:
            pygame.display.set_mode(natrix.rez)

class Opis(natrix.predmet.PredmetSprite):
    """Postoji klon i u "game_options.py"

    """
    def __init__(self, topleft=(200, 200), sprite=None, image_index=0):
        natrix.predmet.PredmetSprite.__init__(self,
                                              sprite, topleft)

        self.image_index = image_index

 #class Save(natrix.predmet.PredmetSprite):
#    def __init__(self, topleft=(200, 200), image_index=0):
#        natrix.predmet.PredmetSprite.__init__(self, sprite_1, topleft)
#
#        self.image_index = image_index
#        natrix.group_sprite.add(self)
#
#    def lmb_down(self):
#        natrix.options[0][0][0].text = str(500)
#        natrix.tree.write('test_xml.txt')




natrix.rooms['room_1'] = natrix.tools.Room()
natrix.rooms['room_2'] = natrix.tools.Room()
natrix.rooms['room_3'] = natrix.tools.Room()
natrix.rooms['room_options'] = natrix.tools.Room()
natrix.rooms['room_res'] = natrix.tools.Room()
natrix.rooms['room_opt_1'] = natrix.tools.Room()
natrix.rooms['room_opt_2'] = natrix.tools.Room()
natrix.rooms['room_opt_3'] = natrix.tools.Room()

# room 0 =================
#natrix.rooms['room_0'].clsarg.append((Save, {'topleft': (900, 50),
#                                             'image_index': 33}))

natrix.rooms['room_0'].static_image = 'plain'

natrix.rooms['room_0'].clsarg.append((Ugasi, {'topleft': (1450, 30),
                                              'image_index': 6}))

natrix.rooms['room_0'].clsarg.append((Goi, {'topleft': (100, 50),
                                            'room_name': 'room_1',
                                            'sprite' : natrix.sprites['buttons'],
                                            'image_index': 0}))

natrix.rooms['room_0'].clsarg.append((Goi, {'topleft': (100, 250),
                                            'room_name': 'room_2',
                                            'sprite' : natrix.sprites['buttons'],
                                            'image_index': 1}))

natrix.rooms['room_0'].clsarg.append((Goi, {'topleft': (100, 450),
                                            'room_name': 'room_3',
                                            'sprite' : natrix.sprites['buttons'],
                                            'image_index': 2}))

natrix.rooms['room_0'].clsarg.append((Goi, {'topleft': (1450, 750),
                                            'room_name': 'room_options',
                                            'sprite' : natrix.sprites['ikone'],
                                            'image_index': 2}))

# room 1 =================
natrix.rooms['room_1'].static_image = 'plain'
natrix.rooms['room_1'].clsarg.append((Goi, {'topleft': (1450, 750),
                                            'room_name': 'room_0',
                                            'sprite' : natrix.sprites['ikone'],
                                            'image_index': 7}))

# room 2 =================
natrix.rooms['room_2'].static_image = 'more'
natrix.rooms['room_2'].clsarg.append((Goi, {'topleft': (1450, 750),
                                            'room_name': 'room_0',
                                            'sprite' : natrix.sprites['ikone'],
                                            'image_index': 7}))

# room 3 =================
natrix.rooms['room_3'].static_image = 'noc'
natrix.rooms['room_3'].clsarg.append((Goi, {'topleft': (1450, 750),
                                            'room_name': 'room_0',
                                            'sprite' : natrix.sprites['ikone'],
                                            'image_index': 7}))

# room options =================
natrix.rooms['room_options'].static_image = 'option'
natrix.rooms['room_options'].clsarg.append((Btn_1, {'topleft': (1450, 750),
                                                    'room_name': 'room_0',
                                                    'sprite' : natrix.sprites['ikone'],
                                                    'image_index': 7}))

natrix.rooms['room_options'].clsarg.append((Btn_def, {'topleft': (1200, 650 + 10),
                                                      'sprite' : natrix.sprites['ikone'],
                                                      'image_index': 8}))

natrix.rooms['room_options'].clsarg.append((Opis, {'topleft': (700, 650),
                                               'sprite' : natrix.sprites['opis'],
                                               'image_index': 5}))


natrix.rooms['room_options'].clsarg.append((Goi, {'topleft': (50, 50),
                                                  'room_name': 'room_res',
                                                  'sprite' : natrix.sprites['buttons'],
                                                  'image_index': 3}))

natrix.rooms['room_options'].clsarg.append((Goi, {'topleft': (50, 250),
                                                  'room_name': 'room_opt_1',
                                                  'sprite' : natrix.sprites['buttons'],
                                                  'image_index': 4}))

natrix.rooms['room_options'].clsarg.append((Goi, {'topleft': (50, 450),
                                                  'room_name': 'room_opt_2',
                                                  'sprite' : natrix.sprites['buttons'],
                                                  'image_index': 5}))

natrix.rooms['room_options'].clsarg.append((Goi, {'topleft': (50, 650),
                                                  'room_name': 'room_opt_3',
                                                  'sprite' : natrix.sprites['buttons'],
                                                  'image_index': 6}))

natrix.rooms['room_options'].clsarg.append((Full_screen, {'topleft': (1450, 50),
                                                    'image_index': 29}))

# room res =================
natrix.rooms['room_res'].static_image = 'option'
natrix.rooms['room_res'].clsarg.append((Goi, {'topleft': (1450, 750),
                                              'room_name': 'room_options',
                                              'sprite' : natrix.sprites['ikone'],
                                              'image_index': 7}))

# room game options 1 =================
natrix.rooms['room_opt_1'].static_image = 'option'
natrix.rooms['room_opt_1'].clsarg.append((Btn_popravi, {'topleft': (1450, 750),
                                            'room_name': 'room_options',
                                            'sprite' : natrix.sprites['ikone'],
                                            'image_index': 7,
                                            'game': 1}))

# room game options 2 =================
natrix.rooms['room_opt_2'].static_image = 'option'
natrix.rooms['room_opt_2'].clsarg.append((Goi, {'topleft': (1450, 750),
                                            'room_name': 'room_options',
                                            'sprite' : natrix.sprites['ikone'],
                                            'image_index': 7}))
# room game options 3 =================
natrix.rooms['room_opt_3'].static_image = 'option'
natrix.rooms['room_opt_3'].clsarg.append((Btn_popravi, {'topleft': (1450, 750),
                                            'room_name': 'room_options',
                                            'sprite' : natrix.sprites['ikone'],
                                            'image_index': 7,
                                            'game': 3}))

import data.game_one
import data.game_two
import data.game_three

import data.game_options
