import random

class Character:
  def __init__(self, health, armor, damage, level, gold, weapon):
    self.health = health
    self.armor = armor
    self.damage = damage
    self.level = level
    self.gold = gold
    self.weapon = "Fists"
new_character = Character(10, 0, 1, 1, 25, "Fists")

class Weapon:
    def __init__(self, name, price, damage):
        self.name = name
        self.price = price
        self.damage = damage

    #Prints the value    
    def __str__(self):
        return f"TEST"

all_weapons = [
  Weapon('Wooden Knuckle Duster', price = 5, damage = 3),
  Weapon('Wooden Sword', price = 10, damage = 5),
  Weapon('Iron Dagger', price = 35, damage = 7),
  Weapon('Iron Sword', price = 75, damage = 9),
  Weapon('Iron Machete', price = 85, damage = 11),
  Weapon('Steel Longsword', price = 125, damage = 16),
  Weapon('Steel Mace', price = 250, damage = 25),
  Weapon('Ray Gun', price = 2147483647, damage = 15000),
  Weapon('Lange Dildo', price = 2147483647, damage = 15000)
]


class Armour:
    def __init__(self, name, price, defence):
        self.name = name
        self.price = price
        self.defence = defence

all_armour = [
  Armour('Leather Sandals', price = 5, defence = 3),
  Armour('Leather Shield', price = 10, defence = 5),
  Armour('Leather Body ', price = 35, defence = 7),
  Armour('Tinfoil Hat', price = 75, defence = 9),
  Armour('Amulet of the Gaylords', price = 125, defence = 10),
  Armour('Steel Skirt', price = 125, defence = 13),
  Armour('Grandmaster Shield', price = 500, defence = 25),
  Armour('Grandmaster Helmet', price = 750, defence = 40),
  Armour('Grandmaster Tassets', price = 1000, defence = 55),
  Armour('Grandmaster Hauberk', price = 1500, defence = 80),
  Armour('Gucci Flip-flops', price = 2147483647, defence = 15000)
]

# a nice way to display your current stats
def stats():
    print(f"******************")
    print(f"**   Level: {new_character.level}   **")
    print(f"**  Health: {new_character.health}  **")
    print(f"**   Armor: {new_character.armor}   **")
    print(f"**   Gold: {new_character.gold}   **")
    print(f"******************")

# class of monster?
class Monster:
  def __init__(self, health, armor, damage, level):
    self.name = name
    self.health = health
    self.armor = armor
    self.damage = damage
    self.level = level
#giant_rat = Monster("giant rat", 3 , 0, 1, 1)


# asks for player name, tells player his current stats + coins 
def introduction():
    print("~~~~~~~~~~          Welcome to Console Warrior          ~~~~~~~~~~\n")
    character_name = input("What is your character\'s name? : ")
    print(f"\nWelcome {character_name}! Your current stats are : \n")
    stats()
    print("\nLet\'s head over to the shop! We can buy weapons and armour there.")
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

            while True:
                try:    
                    input_for_weapon = int(input(f"\nYou have {new_character.gold} coins right now. Enter the number of the item you want to buy or type \'69\' to continue the game : "))
                except ValueError:
                    print("Please enter the number of item you want to buy, or enter \'69\'")
                    continue

                if input_for_weapon == 69:
                    print("CONTINUE GAME")
                elif input_for_weapon in range(0, len(all_weapons)-1) :
                    #selected_weapon = all_weapons[input_for_weapon]
                    #print(f"The weapon you selected is {selected_weapon} ")
                    print(range(0,len(all_weapons)-1))
                    print(f"You chose weapon {input_for_weapon}")
                    answer = input("if you want to buy this item type \'yes\' : ")
                    if answer == 'yes':                                                  #en als je genoeg geld hebt
                        print(f"You bought weapon {input_for_weapon}")
                    else:
                        continue





        elif the_input == 2:
            print("\n      ~~~~~ARMOUR SHOP~~~~~             \n")
            print("__________________________________\n")
            # This will loop through the armours and displays them
            for i, armour in enumerate(all_armour):
                print(f'{i}) {armour.name} - {armour.price} coins - {armour.defence} defence')
            break
        else:
            print("1 or 2 man don\'t be retarded")


selected_weapon = all_weapons[1]
print(selected_weapon)
#print(all_weapons[1])

introduction()
weapon_store()

#play_game()

end_game = input("\n\nBye!!!!!!! :'(")

