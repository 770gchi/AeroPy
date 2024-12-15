import os
import pygame

from .images import Images
from .sounds import Sounds
from .window import Window


class GameConfig:
    def __init__(
            self,
            screen: pygame.Surface,
            clock: pygame.time.Clock,
            fps: int,
            window: Window,
            images: Images,
            sounds: Sounds,
    ):
        self.screen = screen
        self.clock = clock
        self.fps = fps
        self.window = window
        self.images = images
        self.sounds = sounds
        self.debug = os.environ.get("DEBUG", False)
        return None

    def tick(self):
        self.clock.tick(self.fps)
        return None
