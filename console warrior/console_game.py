import random

# class of player
class Character:
  def __init__(self, health, armor, damage, level, gold, weapon):
    self.health = health
    self.armor = armor
    self.damage = damage
    self.level = level
    self.gold = gold
    self.weapon = "none"
new_character = Character(10, 0, 1, 1, 25, "none")


class Weapon:
    def __init__(self, name, price, damage):
        self.name = name
        self.price = price
        self.damage = damage

all_weapons = [
  Weapon('Wooden Knuckle Duster', price=5, damage=3),
  Weapon('Wooden Sword', price=10, damage=5),
  Weapon('Iron Dagger', price=35, damage=7),
  Weapon('Iron Sword', price=75, damage=9),
  Weapon('Iron Machete', price=85, damage=11),
  Weapon('Regenpijp', price=2525, damage=90),
  Weapon('Digna\'s hoofd', price =696969, damage=11000000),
  Weapon('Ray Gun', price=2147483647, damage=15000),
  Weapon('Lange Dildo', price=2147483647, damage=15000)
]


# class of monster?
class Monster:
  def __init__(self, health: int, armor: int, damage: int, level: int):
    self.health = health
    self.armor = armor
    self.damage = damage
    self.level = level
monster = Monster(100, 50, 25, 1)

# asks for player name, tells player his current stats + coins 
def introduction():
    print("~~~~~~~~~~          Welcome to Console Warrior          ~~~~~~~~~~\n")
    character_name = input("What is your character\'s name? : ")
    print(f"\nWelcome {character_name}, you beautiful man! Your warrior is level {new_character.level} with {new_character.health} health and {new_character.armor} armor. You do have {new_character.gold} coins, maybe we can buy you something with that...")
    print("\nLet\'s head over to the weapon / armour shop!")
    return character_name

# nog niks aan gedaan
def play_game():
    while True:
        pass
    else:
        print("BYE!")
        print("BYE!")
        print("BYE!")


# elke keer dat je wapens / armour wilt kopen deze functie uitvoeren
def weapon_store():
    print("\nWelcome to the weapon store of Console Warrior\n")
    while True:
        the_input = 0
        try:
            the_input = int(input("Type \'1\' to see weapons or \'2\' to see armour : ")) #nog optie maken om terug te gaan, maar niet noodzakelijk nog
        except ValueError:
            print("Please enter a valid number boss you dipshit")
            continue
        if the_input == 1:
            print("\n      ~~~~~WEAPONS SHOP~~~~~             \n")
            print("__________________________________\n")
            # This will loop through the weapons and displays them
            for i, weapon in enumerate(all_weapons):
                print(f'{i}) {weapon.name} - {weapon.price} coins - {weapon.damage} damage')
            break
        elif the_input == 2:
            print("ARMOUR")
            break
        else:
            print("1 or 2 man don\'t be retarded")





armour_dict_prices = {
    "Wooden Shoes": 5,
    "Wooden Helmet": 10,
    "Iron Legs": 35,
    "Iron Shield": 75,
    "Iron Chainbody": 85    
    }






introduction()
#play_game()
weapon_store()
end_game = input("\n\nBye!!!!!!! :'(")

