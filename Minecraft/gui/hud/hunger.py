from os.path import join

from Minecraft.gui.hud.base import HUD
from Minecraft.source import path
from Minecraft.utils.utils import *

import pyglet
from pyglet import image
from pyglet.sprite import Sprite


class Hunger(HUD):

    def __init__(self):
        width, height = get_size()
        HUD.__init__(self, width, height)
        self._status = []
        for i in range(9, -1, -1):
            sprite = Sprite(image.load(join(path['texture.hud'], 'hunger.png')),
                x=(width - 450) / 2 + 450 - (i + 1) * 20, y=75)
            self._status.append(sprite)

    def draw(self):
        for item in self._status:
            item.draw()

    def resize(self, width, height):
        for i in range(9, -1, -1):
            self._status[i].position = (width - 450) / 2 + 450 - (i + 1) * 20, 75
