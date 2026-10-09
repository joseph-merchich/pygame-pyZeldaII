#!/usr/local/bin/python
# Copyright (C) Johan Ceuppens 2010

import pygame

class Stateimagelibrary:
    ANIM_SPEED = 5  # advance animation frame every N draws

    def __init__(self):
        self.index = 0
        self.max = 0
        self.list = []
        self._call_count = 0

    def addpicture(self, image):
        self.list.append(image)
        self.max += 1

    def drawstatic(self, screen, xx, yy, index, flip_x=False):
        if self.max == 0:
            return
        img = self.list[index % self.max]
        if flip_x:
            img = pygame.transform.flip(img, True, False)
        screen.blit(img, (xx, yy))

    def draw(self, screen, xx, yy, flip_x=False):
        if self.max == 0:
            return
        if self.index >= self.max:
            self.index = 0
        img = self.list[self.index]
        if flip_x:
            img = pygame.transform.flip(img, True, False)
        screen.blit(img, (xx, yy))
        self._call_count += 1
        if self._call_count >= self.ANIM_SPEED:
            self._call_count = 0
            self.index += 1
