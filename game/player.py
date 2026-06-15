import pygame

from game.entity import Entity
from game.settings import PLAYER_SPEED
from game.resource_path import resource_path


class Player(Entity):

    def __init__(self):

        super().__init__(
            resource_path("assets/images/player.png"),
            600,
            350
        )

    def update(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rect.x -= PLAYER_SPEED

        if keys[pygame.K_d]:
            self.rect.x += PLAYER_SPEED

        if keys[pygame.K_w]:
            self.rect.y -= PLAYER_SPEED

        if keys[pygame.K_s]:
            self.rect.y += PLAYER_SPEED