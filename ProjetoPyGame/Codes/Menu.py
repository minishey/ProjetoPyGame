import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from Codes.Const import WIN_WIDTH


class Menu:
    def __init__(self, screen):
        self.screen_Surface: Surface = screen
        self.surf = pygame.image.load('./asset/Menu_bg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./asset/MenuMusic.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.screen_Surface.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Project", (213, 59, 175), ((WIN_WIDTH / 2), 70))

            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_por: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_por)
        self.screen_Surface.blit(source=text_surf, dest=text_rect)
