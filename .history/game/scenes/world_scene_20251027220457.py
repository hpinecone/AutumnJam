#python imports
import pygame
from pathlib import Path

#game imports
from ..player.model import PlayerData
from ..player.controller import PlayerController
from ..player.render import draw_player
from .base_scene import BaseScene

class WorldScene(BaseScene):
    def on_enter(self):

        pdata = PlayerData()
        self.player = PlayerController(pdata)

        self.font = pygame.font.SysFont(None, 24)
        self.walls = [
            pygame.Rect(50, 80, 860, 20),
            pygame.Rect(50, 440, 860, 20),
            pygame.Rect(50, 100, 20, 360),
            pygame.Rect(890, 100, 20, 360),
            pygame.Rect(500, 240, 100, 20),
        ]
        self.puzzle_trigger = pygame.Rect(780, 360, 100, 60)

    def handle_event(self, event):
        self.player.handle_event(event)

    def update(self, dt):
        self.player.update(dt)
        self.player.collide_with_rects(self.walls)