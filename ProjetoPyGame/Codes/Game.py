import pygame as pygame

from Const import WIN_WIDTH, WIN_HEIGHT
from Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.screen_Surface = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):

        while True:
            menu = Menu(self.screen_Surface)

            menu.run()

