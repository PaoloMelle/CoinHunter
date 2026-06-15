import random

from game.entity import Entity
from game.resource_path import resource_path


class Coin(Entity):

    def __init__(self):

        x = random.randint(50, 1180)
        y = random.randint(50, 620)

        super().__init__(
            resource_path("assets/images/coin.png"),
            x,
            y
        )

    def respawn(self):

        self.rect.x = random.randint(50, 1180)
        self.rect.y = random.randint(50, 620)