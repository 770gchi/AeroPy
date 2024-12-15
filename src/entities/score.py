import pygame
import os
from ..utils import GameConfig
from .entity import Entity


class Score(Entity):
    def __init__(self, config: GameConfig) -> None:
        super().__init__(config)
        self.y = self.config.window.height * 0.1
        self.score = 0
        self.high_score = 0  # 新增：最高分属性

    def reset(self) -> None:
        """重置当前分数，但保留最高分"""
        self.score = 0

    def add(self) -> None:
        """增加分数，更新最高分"""
        self.score += 1
        self.config.sounds.point.play()

        # 更新最高分
        if self.score > self.high_score:
            self.high_score = self.score

    def draw(self) -> None:
        """显示当前分数和最高分"""
        # 绘制当前分数
        score_digits = [int(x) for x in list(str(self.score))]
        images = [self.config.images.numbers[digit] for digit in score_digits]
        digits_width = sum(image.get_width() for image in images)
        x_offset = (self.config.window.width - digits_width) / 2

        for image in images:
            self.config.screen.blit(image, (x_offset, self.y))
            x_offset += image.get_width()

        # 绘制最高分 (位于屏幕顶部右侧)
        high_score_digits = [int(x) for x in list(str(self.high_score))]
        high_score_images = [self.config.images.numbers[digit] for digit in high_score_digits]
        high_score_width = sum(image.get_width() for image in high_score_images)
        high_score_x_offset = self.config.window.width - high_score_width - 20  # 距离右侧 20px
        high_score_y_offset = self.y - 40  # 高于当前分数显示 40px

        for image in high_score_images:
            self.config.screen.blit(image, (high_score_x_offset, high_score_y_offset))
            high_score_x_offset += image.get_width()

        font = pygame.font.Font(None, 20)
        pb_image = font.render("PB", True, (255, 255, 255))  # 创建 PB 文本
        pb_x_offset = high_score_x_offset + 3  # PB在最高分数字右侧，留 5px 间距
        self.config.screen.blit(pb_image, (pb_x_offset, high_score_y_offset))



    def load_high_score(self, file_path: str = "high_score.txt") -> None:
            """加载历史最高分"""
            try:
                # 检查文件是否存在
                if os.path.exists(file_path):
                    with open(file_path, "r") as f:
                        self.high_score = int(f.read().strip())
                else:
                    # 如果文件不存在，则创建并初始化为 0
                    with open(file_path, "w") as f:
                        f.write("0")
            except (ValueError, OSError) as e:
                print(f"Failed to load high score: {e}")
                self.high_score = 0



    def save_high_score(self, file_path: str = "high_score.txt") -> None:
        """Saves the high score to a file."""
        try:
            with open(file_path, "w") as file:
                file.write(str(self.high_score))
        except Exception as e:
            print(f"Failed to save high score: {e}")