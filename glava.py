# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 14:45:47 2017

@author: Lorango
"""

import sys
import pygame
import natrix

#  Main loop.
while True:
    natrix.Controller.clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    natrix.Controller.screen.fill(natrix.yellow)
    pygame.display.update()
