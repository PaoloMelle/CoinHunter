import pygame

from game.entity import Entity
from game.settings import PLAYER_SPEED

# Classe responsável pelo personagem controlado pelo jogador
class Player(Entity):

    def __init__(self):

        super().__init__(
            "assets/images/player.png",
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