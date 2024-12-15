import random
from typing import List, Tuple
import pygame


class Images:
    numbers: List[pygame.Surface]
    game_over: pygame.Surface
    welcome_message: pygame.Surface
    base: pygame.Surface
    background: pygame.Surface
    player: Tuple[pygame.Surface]
    biru: Tuple[pygame.Surface]
    invincible : Tuple[pygame.Surface]

    def __init__(self) -> None:
        self.numbers = list(
            (
                pygame.image.load(f"assets/sprites/{num}.png").convert_alpha()
                for num in range(10)
            )
        )

        # game over sprite
        self.player = pygame.image.load("assets/sprites/plane.png")
        self.game_over = pygame.image.load(
            "assets/sprites/gameover.png"
        ).convert_alpha()
        # welcome_message sprite for welcome screen
        self.welcome_message = pygame.image.load(
            "assets/sprites/message.png"
        ).convert_alpha()
        # base (ground) sprite
        self.base = pygame.image.load("assets/sprites/base.png").convert_alpha()

        self.background = pygame.image.load("assets/sprites/background.png")
        self.biru = (
            pygame.transform.flip(
                pygame.image.load("assets/sprites/biru.png").convert_alpha(),
                False,
                True,
            ),
            pygame.image.load("assets/sprites/biru.png").convert_alpha(),
        )
        self.invincible = pygame.image.load("assets/sprites/invincible.png")



