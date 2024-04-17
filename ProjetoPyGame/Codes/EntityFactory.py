#!/usr/bin/python
#-*- coding: utf-8 -*-

class EntityFactory:
    
    @staticmethod
    def get_entity(entity_name: str, position: tuple):
        match entity_name:
            case 'Level1':
                Backgroud(f'Level1', position)
        pass

