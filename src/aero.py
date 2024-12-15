import asyncio
import sys

import pygame
from pygame.locals import K_ESCAPE, K_SPACE, K_UP, KEYDOWN, QUIT

from .entities import (
    Background,
    Floor,
    GameOver,
    Birus,
    Player,
    PlayerMode,
    Score,
    WelcomeMessage,
    Invincibility
)
from .utils import GameConfig, Images, Sounds, Window

from .entities.player import Invincibility



class Aero:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("让你飞起来模拟器")
        window = Window(288, 512)
        screen = pygame.display.set_mode((window.width, window.height))
        images = Images()

        self.config = GameConfig(
            screen=screen,
            clock=pygame.time.Clock(),
            fps=30,
            window=window,
            images=images,
            sounds=Sounds(),
        )



    async def start(self):
        while True:
            self.background = Background(self.config)
            self.floor = Floor(self.config)
            self.player = Player(self.config)
            self.welcome_message = WelcomeMessage(self.config)
            self.game_over_message = GameOver(self.config)
            self.birus = Birus(self.config)
            self.score = Score(self.config)

            self.score.load_high_score()



            await self.splash()
            await self.play()
            await self.game_over()

            # 检查无敌模式，如果不是无敌状态，才触发游戏结束逻辑
            if Invincibility.flag == False:
                await self.game_over()

    async def splash(self):
        """Shows welcome splash screen animation of flappy bird"""

        self.player.set_mode(PlayerMode.SHM)

        while True:
            for event in pygame.event.get():
                self.check_quit_event(event)
                if self.is_tap_event(event):
                    return

            self.background.tick()
            self.floor.tick()
            self.player.tick()
            self.welcome_message.tick()

            pygame.display.update()
            await asyncio.sleep(0)
            self.config.tick()

    def check_quit_event(self, event):
        if event.type == QUIT or (
            event.type == KEYDOWN and event.key == K_ESCAPE
        ):
            pygame.quit()
            sys.exit()

    def is_tap_event(self, event):
        m_left, _, m_right = pygame.mouse.get_pressed()

        space_or_up = event.type == KEYDOWN and (
            event.key == K_SPACE or event.key == K_UP
        )
        screen_tap = event.type == pygame.FINGERDOWN

        if m_right:  # 如果右键被按下
            Invincibility.flag = not Invincibility.flag  # 切换无敌模式
            print(f"无敌模式: {'开启' if Invincibility.flag else '关闭'}")  # 打印无敌状态
            return False  # 返回 False 避免冲突


        return m_left or space_or_up or screen_tap




    async def play(self):
        self.score.reset()
        self.player.set_mode(PlayerMode.NORMAL)



        while True:

            self.player.img_switch()

            if not Invincibility.flag and self.player.collided(self.birus, self.floor):
                return


            for i, biru in enumerate(self.birus.upper):
                if self.player.crossed(biru):
                    self.score.add()

            for event in pygame.event.get():

                self.check_quit_event(event)  # existing quit checks




                self.check_quit_event(event)
                if self.is_tap_event(event):
                    self.player.flap()






            self.background.tick()
            self.floor.tick()
            self.birus.tick()
            self.score.tick()
            self.player.tick()

            pygame.display.update()
            await asyncio.sleep(0)
            self.config.tick()

    async def game_over(self):
        """crashes the player down and shows gameover image"""

        if Invincibility.flag == True :
            print("Player is in INVINCIBLE mode. Skipping game over.")
            return

        self.player.set_mode(PlayerMode.CRASH)
        self.birus.stop()
        self.floor.stop()
        self.score.save_high_score()

        while True:
            for event in pygame.event.get():
                self.check_quit_event(event)
                if self.is_tap_event(event):
                    if self.player.y + self.player.h >= self.floor.y - 1:
                        return

            self.background.tick()
            self.floor.tick()
            self.birus.tick()
            self.score.tick()
            self.player.tick()
            self.game_over_message.tick()

            self.config.tick()
            pygame.display.update()
            await asyncio.sleep(0)