import pygame as pygame
from pygame import Surface, Rect
from pygame.font import Font

from Codes.Const import WIN_WIDTH, WIN_HEIGHT
from Codes.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.screen_Surface = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):

        while True:
            menu = Menu(self.screen_Surface)

            menu.run()