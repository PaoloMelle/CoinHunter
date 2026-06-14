import pygame

from game.settings import *

# Gerencia a interface principal e a navegação do menu do jogo
class Menu:

    def __init__(self):

        self.options = [
            "JOGAR FACIL",
            "JOGAR DIFICIL",
            "SCORES",
            "SAIR"
        ]

        self.selected = 0
        self.option_rects = []

        self.background = pygame.image.load(
            "assets/images/menu/menu_background.png"
        )

        self.background = pygame.transform.scale(
            self.background,
            (SCREEN_WIDTH, SCREEN_HEIGHT)
        )

        self.title_font = pygame.font.SysFont(
            "arial",
            70,
            bold=True
        )

        self.option_font = pygame.font.SysFont(
            "arial",
            40
        )

# Processa eventos de teclado e mouse do menu
    def handle_event(self, event):

        if event.type == pygame.MOUSEMOTION:

            mouse_pos = pygame.mouse.get_pos()

            for index, rect in enumerate(self.option_rects):

                if rect.collidepoint(mouse_pos):
                    self.selected = index

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1:

                for index, rect in enumerate(self.option_rects):

                    if rect.collidepoint(event.pos):
                        return self.options[index]

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:

                self.selected -= 1

                if self.selected < 0:
                    self.selected = len(self.options) - 1

            elif event.key == pygame.K_DOWN:

                self.selected += 1

                if self.selected >= len(self.options):
                    self.selected = 0

            elif event.key == pygame.K_RETURN:

                return self.options[self.selected]

        return None

    # Desenha todos os elementos visuais do menu na tela
    def draw(self, screen):

        screen.blit(
            self.background,
            (0, 0)
        )

        overlay = pygame.Surface(
            (SCREEN_WIDTH, SCREEN_HEIGHT)
        )

        overlay.set_alpha(120)

        overlay.fill((0, 0, 0))

        screen.blit(
            overlay,
            (0, 0)
        )

        title = self.title_font.render(
            "COIN HUNTER",
            True,
            GOLD
        )

        title_rect = title.get_rect(
            center=(SCREEN_WIDTH // 2, 150)
        )

        screen.blit(title, title_rect)

        self.option_rects.clear()

        for index, option in enumerate(self.options):

            color = WHITE

            if index == self.selected:
                color = GOLD

            text = self.option_font.render(
                option,
                True,
                color
            )

            text_rect = text.get_rect(
                center=(
                    SCREEN_WIDTH // 2,
                    300 + index * 70
                )
            )

            screen.blit(text, text_rect)

            self.option_rects.append(
                text_rect.copy()
            )

        controls_font = pygame.font.SysFont(
            "arial",
            18
        )

        controls = [

            "CONTROLES",

            "",

            "WASD   - Movimentar",

            "↑ ↓     - Navegar Menu",

            "ENTER - Selecionar",

            "ESC    - Voltar"

        ]

        for index, text in enumerate(controls):
            color = GOLD if index == 0 else WHITE

            render = controls_font.render(
                text,
                True,
                color
            )

            screen.blit(
                render,
                (
                    40,
                    560 + index * 24
                )
            )