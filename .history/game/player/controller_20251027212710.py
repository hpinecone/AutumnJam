import pygame
from .model import PlayerData

class PlayerController:
    def __init__(self, data: PlayerData):
        self.data = data
        self._vel = pygame.Vector2(0,0)

    def handle_event():
        pass

    def update(self, dt: float):
        keys = pygame.key.get_pressed()
        self._vel.xy = 0, 0
        if keys[pygame.K_w]: self.vel.y -= 1
        if keys[pygame.K_a]: self._vel.x -= 1
        if keys[pygame.K_s]: self.vel.y +=1;
        if keys[pygame.K_d]: self.vel.x += 1
        