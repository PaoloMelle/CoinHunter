import pygame

# Controla os efeitos sonoros do jogo
class SoundManager:

    @staticmethod
    def initialize():

        pygame.mixer.init()

        SoundManager.coin = pygame.mixer.Sound(
            "assets/sounds/coin.wav"
        )

        SoundManager.menu = pygame.mixer.Sound(
            "assets/sounds/menu.wav"
        )

        SoundManager.victory = pygame.mixer.Sound(
            "assets/sounds/victory.wav"
        )

        SoundManager.defeat = pygame.mixer.Sound(
            "assets/sounds/defeat.wav"
        )

        pygame.mixer.music.load(
            "assets/sounds/menu_music.mp3"
        )

        pygame.mixer.music.set_volume(
            0.3
        )

        SoundManager.coin.set_volume(0.5)

        SoundManager.menu.set_volume(0.5)

        SoundManager.victory.set_volume(0.7)

        SoundManager.defeat.set_volume(0.7)

    @staticmethod
    def play_menu_music():
        pygame.mixer.music.play(-1)

    @staticmethod
    def stop_music():
        pygame.mixer.music.stop()


    @staticmethod
    def play_coin():

        SoundManager.coin.play()

    @staticmethod
    def play_menu():

        SoundManager.menu.play()

    @staticmethod
    def play_victory():

        SoundManager.victory.play()

    @staticmethod
    def play_defeat():

        SoundManager.defeat.play()