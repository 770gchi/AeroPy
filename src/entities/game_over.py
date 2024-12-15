from ..utils import GameConfig
from .entity import Entity


class GameOver(Entity):
    def __init__(self, config: GameConfig) :
        super().__init__(
            config=config,
            image=config.images.game_over,
            x=(config.window.width - config.images.game_over.get_width()) // 2,
            y=int(config.window.height * 0.2),
        )
        return None

"""人终有一死 而有的人则需要一点小小的帮助"""