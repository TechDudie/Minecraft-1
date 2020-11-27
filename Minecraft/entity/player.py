from Minecraft.entity.entity import Entity
from Minecraft.source import path
from Minecraft.utils.utils import *

from pyglet import graphics

class Player(Entity):

    def __init__(self):
        super(Player, self).__init__(position=(0, 0, 0), rotation=(0, 0))
        # 玩家模型
        self.batch = graphics.Batch()
        # 玩家的各个部分
        self.player = {}
        # 状态
        self.status = {}
        self.status['strafe'] = [0, 0]
        self.status['position'] = (0, 0, 0)

    def draw(self):
        self.batch.draw()
