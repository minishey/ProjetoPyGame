import sys

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from Codes.Const import WIN_WIDTH, COLOR_RED, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW


class Menu:
    def __init__(self, screen):
        self.screen_Surface: Surface = screen
        self.surf = pygame.image.load('./asset/Menu_bg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./asset/MenuMusic.mp3')
        pygame.mixer_music.play(-1)
        menu_option = 0
        while True:
            self.screen_Surface.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Project", COLOR_RED, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "PyGame", COLOR_RED, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, (WIN_WIDTH / 2, 200 + 30 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, (WIN_WIDTH / 2, 200 + 30 * i))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.screen_Surface.blit(source=text_surf, dest=text_rect)
