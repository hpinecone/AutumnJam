#python imports
import pygame
from pathlib import Path

#game imports
from ..player.model import PlayerData
from ..player.controller import PlayerController
from ..player.render import draw_player

class WorldScene(BaseScene):

    def handle_event(self, event):
        self.player.handle_event(event)

    def update(self, dt):
        self.player.update(dt)
        self.player.collide_with_rects(self.walls)