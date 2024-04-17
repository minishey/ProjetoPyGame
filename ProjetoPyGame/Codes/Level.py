from Codes import Entity

class Level:
    def __init__(self, screen, name, menu_option):
        self.screen_Surface = screen
        self.entity_list = name
        self.mode = menu_option  # Opção do menu
        self.entity_list: list[Entity] = []
        self.entity_list.append(EntityFactory.get_entity('Level1', (0, 0)))
    
    
    def run(self, ):
        while True: 
            for ent in self.entity_list:
                
        pass
