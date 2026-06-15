import pygame

from game.settings import *
from game.menu import Menu
from game.game_manager import GameManager
from game.sound_manager import SoundManager
from game.score_screen import ScoreScreen
from game.resource_path import resource_path

pygame.init()

SoundManager.initialize()

SoundManager.play_menu_music()

icon = pygame.image.load(
    resource_path(
        "assets/images/icon.png"
    )
)

pygame.display.set_icon(icon)

screen = pygame.display.set_mode(
    (SCREEN_WIDTH, SCREEN_HEIGHT)
)

pygame.display.set_caption(
    GAME_TITLE
)

clock = pygame.time.Clock()

menu = Menu()

score_screen = ScoreScreen()

current_screen = "menu"

game = None

font = pygame.font.SysFont(
    "arial",
    30
)

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                current_screen = "menu"

        result = menu.handle_event(event)

        if result:

            SoundManager.play_menu()

            print(
                f"Selecionado: {result}"
            )

            if result == "JOGAR FACIL":

                game = GameManager("easy")

                current_screen = "game"

            elif result == "JOGAR DIFICIL":

                game = GameManager("hard")

                current_screen = "game"

            elif result == "SCORES":

                current_screen = "scores"

            elif result == "SAIR":
                running = False

    screen.fill((20, 120, 20))

    if current_screen == "menu":

        menu.draw(screen)

    elif current_screen == "scores":

        score_screen.draw(screen)

    elif current_screen == "game":

        game.update()

        game.draw(
            screen,
            font
        )

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()