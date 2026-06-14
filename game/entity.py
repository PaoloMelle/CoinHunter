import pygame
from abc import ABC

# Classe abstrata base utilizada pelas entidades do jogo
class Entity(ABC):

    def __init__(self, image_path, x, y):

        self.image = pygame.image.load(
            image_path
        ).convert_alpha()

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):

        screen.blit(
            self.image,
            self.rect
        )