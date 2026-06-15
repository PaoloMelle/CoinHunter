import pygame

from game.resource_path import resource_path


class BackgroundLayer:

    def __init__(self, image_path, speed, y_position):

        self.image = pygame.image.load(
            resource_path(image_path)
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image,
            (1280, 720)
        )

        self.speed = speed
        self.x = 0
        self.y = y_position

    def update(self):

        self.x -= self.speed

        width = self.image.get_width()

        if self.x <= -width:
            self.x = 0

    def draw(self, screen):

        width = self.image.get_width()

        screen.blit(self.image, (self.x, self.y))
        screen.blit(self.image, (self.x + width, self.y))