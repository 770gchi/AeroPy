import asyncio

from src.aero import Aero


print("开始游戏请按空格或鼠标左键或方向键上键")
print("按鼠标右键开启无敌模式")
print("祝您游戏愉快")

if __name__ == "__main__":
    asyncio.run(Aero().start())
