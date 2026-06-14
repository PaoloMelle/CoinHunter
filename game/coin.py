import random

from game.entity import Entity

# Classe responsável pela moeda coletável do jogo
class Coin(Entity):

    def __init__(self):

        x = random.randint(50, 1180)
        y = random.randint(50, 620)

        super().__init__(
            "assets/images/coin.png",
            x,
            y
        )

    def respawn(self):

        self.rect.x = random.randint(
            50,
            1180
        )

        self.rect.y = random.randint(
            50,
            620
        )