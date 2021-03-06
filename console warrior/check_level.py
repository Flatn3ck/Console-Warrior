from classes import *
from functions import *
from items import *

# Gonna have to rewrite a lot of it if the game gets any bigger 
#Check experience and checks if you level up, gives you extra health per gained level

def check_level(check_exp):
    if new_character.experience < 83:
        new_character.level = 1
        new_character.health = 13
    elif new_character.experience > 82 and new_character.experience < 140:
        new_character.level = 2
        new_character.health = 16
    elif new_character.experience > 139 and new_character.experience < 200:
        new_character.level = 3
        new_character.health = 19
    elif new_character.experience > 199 and new_character < 300:
        new_character.level = 4
        new_character.health = 22
    else:
        new_character.level = 5
        new_character.health = 25
    return new_character.level, new_character.health