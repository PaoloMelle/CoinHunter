import pygame

from game.player import Player
from game.coin import Coin
from game.score import ScoreManager
from game.sound_manager import SoundManager
from game.background_manager import BackgroundManager
from game.settings import *

# Classe responsável por controlar a lógica principal do jogo
class GameManager:

    def __init__(self, mode):

        self.mode = mode

        self.background = BackgroundManager()

        self.player = Player()

        self.coin = Coin()

        self.coins_collected = 0

        self.game_over = False

        self.victory = False

        self.final_time = None

        if mode == "easy":

            self.goal = EASY_GOAL

            self.time_limit = EASY_TIME

        else:

            self.goal = HARD_GOAL

            self.time_limit = HARD_TIME

        self.start_ticks = pygame.time.get_ticks()

    def update(self):

        if self.game_over:
            return

        self.background.update()

        self.player.update()

        if self.player.rect.colliderect(self.coin.rect):

            self.coins_collected += 1

            SoundManager.play_coin()

            self.coin.respawn()

        elapsed_time = (
            pygame.time.get_ticks() - self.start_ticks
        ) // 1000

        remaining_time = self.time_limit - elapsed_time

        if self.coins_collected >= self.goal:

            ScoreManager.save_score(
                self.coins_collected,
                self.mode
            )

            self.final_time = self.get_remaining_time()

            SoundManager.play_victory()

            self.victory = True

            self.game_over = True


        elif remaining_time <= 0:

            ScoreManager.save_score(
                self.coins_collected,
                self.mode
            )

            self.final_time = self.get_remaining_time()

            SoundManager.play_defeat()

            self.victory = False

            self.game_over = True

    def get_remaining_time(self):

        if self.game_over:
            return self.final_time

        elapsed_time = (
                               pygame.time.get_ticks() - self.start_ticks
                       ) // 1000

        remaining = self.time_limit - elapsed_time

        return max(0, remaining)

    def draw(self, screen, font):

        self.background.draw(screen)

        self.player.draw(screen)

        self.coin.draw(screen)

        score_text = font.render(
            f"Moedas: {self.coins_collected}/{self.goal}",
            True,
            WHITE
        )

        screen.blit(
            score_text,
            (20, 20)
        )

        timer_text = font.render(
            f"Tempo: {self.get_remaining_time()}",
            True,
            WHITE
        )

        screen.blit(
            timer_text,
            (20, 60)
        )

        if self.game_over:

            overlay = pygame.Surface(
                (
                    SCREEN_WIDTH,
                    SCREEN_HEIGHT
                )
            )

            overlay.set_alpha(180)

            overlay.fill((0, 0, 0))

            screen.blit(
                overlay,
                (0, 0)
            )

            if self.victory:

                result_text = font.render(
                    "VOCE VENCEU!",
                    True,
                    GREEN
                )

            else:

                result_text = font.render(
                    "VOCE PERDEU!",
                    True,
                    RED
                )

            rect = result_text.get_rect(
                center=(
                    SCREEN_WIDTH // 2,
                    SCREEN_HEIGHT // 2 - 40
                )
            )

            screen.blit(
                result_text,
                rect
            )

            info_text = font.render(
                "ESC - VOLTAR AO MENU",
                True,
                WHITE
            )

            info_rect = info_text.get_rect(
                center=(
                    SCREEN_WIDTH // 2,
                    SCREEN_HEIGHT // 2 + 30
                )
            )

            screen.blit(
                info_text,
                info_rect
            )