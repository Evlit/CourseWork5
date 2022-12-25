from classes import unit_classes
from equipment import Equipment

equipment = Equipment()
heroes = {}


def get_result(title: str):
    """Функция создания словаря для выбора персонажа игры """
    result = {
        "header": title,  # для названия страниц
        "classes": unit_classes,  # для названия классов
        "weapons": equipment.get_weapons_names(),  # для названия оружия
        "armors": equipment.get_armors_names()  # для названия брони
    }
    return result


def get_heroes(key_, value_):
    """
    Функция создания и возврата словаря игроков
    """
    if key_ and value_:
        heroes[key_] = value_
    else:
        return heroes
