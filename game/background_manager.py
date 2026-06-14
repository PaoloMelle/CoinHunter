from game.background_layer import BackgroundLayer

# Gerencia as camadas do efeito Parallax
class BackgroundManager:

    def __init__(self):

        self.layers = [

            BackgroundLayer(
                "assets/images/background/sky.png",
                0.2,
                0
            ),

            BackgroundLayer(
                "assets/images/background/mountains.png",
                0.5,
                120
            ),

            BackgroundLayer(
                "assets/images/background/trees.png",
                1.0,
                350
            )

        ]

    def update(self):

        for layer in self.layers:

            layer.update()

    def draw(self, screen):

        for layer in self.layers:

            layer.draw(screen)