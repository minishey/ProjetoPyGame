from Codes import Entity

class Level:
    def __init__(self, screen, name, menu_option):
        self.screen_Surface = screen
        self.entity_list = name
        self.mode = menu_option  # Opção do menu
        self.entity_list: list[Entity] = []

    def run(self, ):
        pass
