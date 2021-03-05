from classes import *
from items import *
import time

def print_and_sleep(text, seconds):
  print(text)
  time.sleep(seconds)

# asks for player name, tells player his current stats + coins 
def introduction():
    time.sleep(1)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("~~~~~~~~~~Welcome to Console Warrior~~~~~~~~~~\n")
    print_and_sleep("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n",1)
    print_and_sleep("This is not a rip off of Sword Art Online.....\n",1)
    print_and_sleep("Your goal is to clear all 100 floors.....\n",1)
    print_and_sleep("You probably won\'t win this game.....\n",1)
    print_and_sleep("Great adventures are waiting on you..... \n",1)
    print_and_sleep("Scary bosses are waiting you at the end of each floor..... \n",1)
    print_and_sleep("There is no Asuna here.. you weeb.....",1)
    print_and_sleep("\nLet\'s start.....\n",1)
    time.sleep(0.5)
    character_name = input("What is your character\'s name? : ")
    time.sleep(0.5)
    print_and_sleep(f"\nWelcome {character_name}! Your current stats are : \n",2)
    stats()
    print_and_sleep("\nLet\'s head over to the market and visit the weapons and armour shop.", 1)
    return character_name
    weapon_store()

def stats():
    print(f"******************")
    print(f"**   Level: {new_character.level}   **")
    print(f"**  Health: {new_character.health}  **")
    print(f"**   Armor: {new_character.armor}   **")
    print(f"**   Gold: {new_character.gold}   **")
    print_and_sleep(f"******************\n", 0.5)
    print_and_sleep(f"Your current weapon is: {new_character.weapon}",0.5)
    print_and_sleep(f"Your current armour is: {new_character.gear}",0.5)
    print_and_sleep(f"Your current damage is: {new_character.damage}",0.5)
    print_and_sleep(f"Your current experience points are: {new_character.experience}",0.5)
    print_and_sleep(f"You\'ll need {83-new_character.experience} exp to reach level {new_character.level+1}",0.5)



# elke keer dat je wapens / armour wilt kopen deze functie uitvoeren
def weapon_store():
    print_and_sleep("\nWelcome to the market of Floor 1\n", 2)
    print_and_sleep("- Type \'1\' to see the weaponshop  \n- Type \'2\' to see the armourshop \n- Type \'3\' to continue your adventure. \n\n",1)
    while True:
        try:
            the_input = int(input(f"Don\'t start playing with no gear, you\'ll die. : "))
        except ValueError:
            print("Please enter a valid number boss you dipshit")
            continue

        if the_input == 1:
            time.sleep(1)
            print("\n      ~~~~~WEAPONS SHOP~~~~~             \n")
            print("__________________________________\n")

            # This will loop through the weapons and displays them
            for i, weapon in enumerate(all_weapons):
                time.sleep(0.25)
                print(f'{i}) {weapon.name} - {weapon.price} coins - {weapon.damage} damage')

            while True:
                try:    
                    input_for_weapon = int(input(f"\nYou have {new_character.gold} coins right now. Enter the number of the item you want to buy or type \'69\' to return to the previous screen : "))
                except ValueError:
                    print("Please enter the number of item you want to buy, or enter \'69\' to return to the previous screen")
                    continue

                if input_for_weapon == 69:
                    print("\n")
                    break
                elif input_for_weapon in range(0, len(all_weapons)-1) :
                    selected_weapon = all_weapons[input_for_weapon].name
                    selected_weapon_price = all_weapons[input_for_weapon].price
                    selected_weapon_damage = all_weapons[input_for_weapon].damage
                    print(f"\nThe weapon you selected is {selected_weapon} and it costs {selected_weapon_price} coins \n")
                    time.sleep(1)
                    answer = input("if you want to buy this item type \'yes\' : ")

                    if answer == 'yes' and new_character.gold >= selected_weapon_price :  
                        new_character.gold = new_character.gold - selected_weapon_price
                        new_character.weapon = selected_weapon
                        new_character.damage += selected_weapon_damage                                              
                        print(f"\nYou bought a {selected_weapon} and you have {new_character.gold} coins left.\n")
                        weapon_store()
                        return new_character.weapon, new_character.gold, new_character.damage
                        
                    elif answer == 'yes' and new_character.gold < selected_weapon_price:
                        print(f"\nYou don\'t have enough money to purchase {selected_weapon}")
                        weapon_store()
                    else:
                        print("\nType \'yes\' to buy it.")

######################################################################################################################################################################

        elif the_input == 2:
            time.sleep(1)
            print("\n      ~~~~~ARMOUR SHOP~~~~~             \n")
            print("__________________________________\n")
            # This will loop through the armours and displays them
            for i, armour in enumerate(all_armour):
                time.sleep(0.25)
                print(f'{i}) {armour.name} - {armour.price} coins - {armour.defence} defence')
            
            while True:
                try:    
                    input_for_armour = int(input(f"\nYou have {new_character.gold} coins right now. Enter the number of the item you want to buy or type \'69\' to return to the previous screen : "))
                except ValueError:
                    print("Please enter the number of item you want to buy, or enter \'69\' to return to the previous screen")
                    continue

                if input_for_armour == 69:
                    print("\n")
                    break
                elif input_for_armour in range(0, len(all_armour)-1) :
                    selected_armour = all_armour[input_for_armour].name
                    selected_armour_defence = all_armour[input_for_armour].defence
                    selected_armour_price = all_armour[input_for_armour].price
                    print(f"\nThe armour you selected is {selected_armour} and it costs {selected_armour_price} coins \n")
                    answer = input("if you want to buy this item type \'yes\' : ")

                    if answer == 'yes' and new_character.gold >= selected_armour_price :  
                        new_character.gold = new_character.gold - selected_armour_price
                        new_character.gear = selected_armour    
                        new_character.armor += all_armour[input_for_armour].defence                                         
                        print(f"\nYou bought a {selected_armour} and you have {new_character.gold} coins left.\n")
                        weapon_store()
                        return new_character.gear, new_character.gold, new_character.armor
                    elif answer == 'yes' and new_character.gold < selected_armour_price:
                        print(f"\nYou don\'t have enough money to purchase {selected_armour}")
                        weapon_store()
                    else:
                        print("\nType \'yes\' to buy it.")

######################################################################################################################################################################

        elif the_input == 3:
            if new_character.gold == 25:
                print("\nWhat did I just say? You will die without weapons or gear, go buy some you moron!")
                weapon_store()
            else:
                continue_adventure()
        else:
            print("1, 2 or 3 man don\'t be retarded")







def continue_adventure():
    print("\nYou got 4 options : \n")
    options_input = int(input(f"- Type \'1\' to train your combat and level up  \n- Type \'2\' to see your stats and gear \n- Type \'3\' to check out the shops. \n- Type \'4\' to fight the boss of this floor (available at level 5) : "))
    if options_input == 1:
        print_and_sleep("\n~~~~~List of monsters to fight~~~~~ \n", 0.5)
        for i, monster in enumerate(all_monsters):
            time.sleep(0.25)
            print(f'{i}) {monster.name} - level {monster.level}  - {monster.health} health - {monster.damage} damage - {monster.armor} defence')


        while True:
                try:    
                    input_for_fight = int(input(f"\nYou have {len(all_monsters)} options to fight. Enter the number of the monster you want to fight or type \'69\' to return to the previous screen : "))
                except ValueError:
                    print("Please enter the number of the monster you want to fight, or enter \'69\' to return to the previous screen")
                    continue   
        
                if input_for_fight == 69:
                    print("\n")
                    continue_adventure()
                elif input_for_fight in range(0, len(all_monsters)) :
                    selected_monster = all_monsters[input_for_fight].name
                    print(f"\nThe monster you selected is {selected_monster}, are you sure you can handle that? ")
                    answer = input("\nIf you can handle it type \'yes\' or typ \'back\' to go back : ")
                    if answer == 'yes':
                        print_and_sleep(f"\nSo you want to try to kill {selected_monster}... With a {new_character.weapon}?? gooood luck..\n", 0.5)
                        fight(selected_monster)
                        continue_adventure()
                    elif answer == 'back':
                        continue_adventure()
                    else:
                        print("Returning to previous screen...")
    elif options_input == 2:
        stats()
        continue_adventure()
    elif options_input == 3:
        weapon_store()
        continue_adventure
    elif options_input == 4:
        if new_character.level < 5:
            print("\nYou have to get to level 5 before you even try this..")
            continue_adventure()
        else:
            print("Let\'s kill the boss")
            continue_adventure()


def fight(selected_monster):
    print_and_sleep(f"- Type \'1\' to attack the {selected_monster} \n- Type \'2\' to eat food or drink a potion (not available yet) \n- Type \'3\' to run away!. \n",0.5)
    fight_input = int(input("\nWhat do you want to do? : "))
    if fight_input == 1:
        print_and_sleep(f"\nYou hit the {selected_monster} right in the kisser! his health is now {selected_monster.health} but he will attack you now!",1)
        print_and_sleep(f"\nThe {selected_monster} hits back! your health is now {new_character.health} but it's your turn to fight now!",1)
        blabla = int(input("yo"))
    elif fight_input == 2:
        print(f"\nnot available yet, sorry!")
        continue_adventure()
    elif fight_input == 3:
        print("\nYou ran away!! coward.....")
        continue_adventure()
    else:
        fight()














# nog niks aan gedaan
def play_game():
    introduction()
    weapon_store()


