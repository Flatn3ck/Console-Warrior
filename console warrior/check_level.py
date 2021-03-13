from classes import *
from functions import *
from items import *

# Gonna have to rewrite a lot of it if the game gets any bigger 
#Check experience and checks if you level up, gives you extra health per gained level

def check_level(check_exp):
    if new_character.experience < 83:
        new_character.level = 1
        #new_character.health = 10 
    elif new_character.experience > 82 and new_character.experience < 174:
        new_character.level = 2
        #new_character.health = 13 
    elif new_character.experience > 173 and new_character.experience < 276:
        new_character.level = 3
        #new_character.health = 16 
    elif new_character.experience > 275 and new_character.experience < 388:
        new_character.level = 4
        #new_character.health = 19 
    elif new_character.experience > 387 and new_character.experience < 512:
        new_character.level = 5
        #new_character.health = 22 
    elif new_character.experience > 511 and new_character.experience < 650:
        new_character.level = 6
        #new_character.health = 22 
    elif new_character.experience > 649 and new_character.experience < 801:
        new_character.level = 7
        #new_character.health = 25  
    elif new_character.experience > 800 and new_character.experience < 969:
        new_character.level = 8
        #new_character.health = 28 
    elif new_character.experience > 968 and new_character.experience < 1154:
        new_character.level = 9
        #new_character.health = 31 
    else:
        new_character.level = 10
        #new_character.health = 34 
    return new_character.level, new_character.health, new_character.health


    # Level 1 = 0 exp
    # Level 2 = 83 exp
    # Level 3 = 174 exp
    # level 4 = 276 exp
    # level 5 = 388 exp
    # level 6 = 512 exp
    # level 7 = 650 exp
    # level 8 = 801 exp
    # level 9 = 969 exp    
    # level 10 = 1154 exp