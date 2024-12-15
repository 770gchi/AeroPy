import random
from typing import List

from ..utils import GameConfig
from .entity import Entity

"""biru stands for building in japanese so this is it"""
"""this game was not suppose to have any metaphor for 911, rip"""

class Biru(Entity):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.vel_x = -5

    def draw(self) -> None:
        self.x += self.vel_x
        super().draw()

class Birus(Entity):
    upper: List[Biru]
    lower: List[Biru]

    def __init__(self, config: GameConfig) -> None:
        super().__init__(config)
        self.biru_gap = 120
        self.top = 0
        self.bottom = self.config.window.viewport_height
        self.upper = []
        self.lower = []
        self.spawn_initial_birus()

    def tick(self) -> None:
        if self.can_spawn_birus():
            self.spawn_new_birus()
        self.remove_old_birus()

        for up_biru, low_biru in zip(self.upper, self.lower):
            up_biru.tick()
            low_biru.tick()

    def stop(self) -> None:
        for biru in self.upper + self.lower:
            biru.vel_x = 0

    def can_spawn_birus(self) -> bool:
        last = self.upper[-1]
        if not last:
            return True

        return self.config.window.width - (last.x + last.w) > last.w * 2.5

    def spawn_new_birus(self):
        # add new building when first building is about to touch left of screen
        upper, lower = self.make_random_birus()
        self.upper.append(upper)
        self.lower.append(lower)

    def remove_old_birus(self):
        # remove first building if its out of the screen
        for biru in self.upper:
            if biru.x < -biru.w:
                self.upper.remove(biru)

        for biru in self.lower:
            if biru.x < -biru.w:
                self.lower.remove(biru)

    def spawn_initial_birus(self):
        upper_1, lower_1 = self.make_random_birus()
        upper_1.x = self.config.window.width + upper_1.w * 3
        lower_1.x = self.config.window.width + upper_1.w * 3
        self.upper.append(upper_1)
        self.lower.append(lower_1)

        upper_2, lower_2 = self.make_random_birus()
        upper_2.x = upper_1.x + upper_1.w * 3.5
        lower_2.x = upper_1.x + upper_1.w * 3.5
        self.upper.append(upper_2)
        self.lower.append(lower_2)

    def make_random_birus(self):
        """returns a randomly generated buildings"""
        # y of gap between upper and lower building
        base_y = self.config.window.viewport_height

        gap_y = random.randrange(0, int(base_y * 0.6 - self.biru_gap))
        gap_y += int(base_y * 0.2)
        biru_height = self.config.images.biru[0].get_height()
        biru_x = self.config.window.width + 10

        upper_biru = Biru(
            self.config,
            self.config.images.biru[0],
            biru_x,
            gap_y - biru_height,
        )

        lower_biru = Biru(
            self.config,
            self.config.images.biru[1],
            biru_x,
            gap_y + self.biru_gap,
        )

        return upper_biru, lower_biru