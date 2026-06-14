import pygame

from game.score import ScoreManager
from game.settings import *

# Gerencia a leitura e gravação dos rankings
class ScoreScreen:

    def __init__(self):

        self.title_font = pygame.font.SysFont(
            "arial",
            50
        )

        self.text_font = pygame.font.SysFont(
            "arial",
            30
        )

    def draw(self, screen):

        screen.fill((20, 20, 20))

        title = self.title_font.render(
            "TOP SCORES",
            True,
            GOLD
        )

        screen.blit(
            title,
            title.get_rect(
                center=(SCREEN_WIDTH // 2, 80)
            )
        )

        easy_scores = ScoreManager.load_scores(
            "easy"
        )

        hard_scores = ScoreManager.load_scores(
            "hard"
        )

        easy_title = self.text_font.render(
            "TOP 5 FACIL",
            True,
            WHITE
        )

        screen.blit(
            easy_title,
            (250, 180)
        )

        for index, score in enumerate(
                easy_scores):

            text = self.text_font.render(
                f"{index + 1}º  {score}",
                True,
                WHITE
            )

            screen.blit(
                text,
                (
                    250,
                    230 + index * 40
                )
            )

        hard_title = self.text_font.render(
            "TOP 5 DIFICIL",
            True,
            WHITE
        )

        screen.blit(
            hard_title,
            (750, 180)
        )

        for index, score in enumerate(
                hard_scores):

            text = self.text_font.render(
                f"{index + 1}º  {score}",
                True,
                WHITE
            )

            screen.blit(
                text,
                (
                    750,
                    230 + index * 40
                )
            )

        info = self.text_font.render(
            "ESC - VOLTAR",
            True,
            GOLD
        )

        screen.blit(
            info,
            info.get_rect(
                center=(
                    SCREEN_WIDTH // 2,
                    650
                )
            )
        )