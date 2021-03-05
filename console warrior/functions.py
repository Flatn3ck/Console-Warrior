from classes import *
from items import *
import time
import random


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
                    answer = input("If you want to buy this item type \'yes\' : ")

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
                        weapon_store()
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
                elif input_for_fight in range(0, len(all_monsters)-1) :
                    selected_monster = all_monsters[input_for_fight].name
                    print(f"\nThe monster you selected is {selected_monster}, are you sure you can handle that? ")
                    answer = input("\nIf you can handle it type \'yes\' or typ \'back\' to go back : ")
                    if answer == 'yes':
                        print_and_sleep(f"\nSo you want to try to kill {selected_monster}... With a {new_character.weapon}?? gooood luck..\n", 0.5)
                        fight(selected_monster,input_for_fight)
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


def fight(selected_monster, input_for_fight):
    print_and_sleep(f"- Type \'1\' to attack the {selected_monster} \n- Type \'2\' to eat food or drink a potion (not available yet) \n- Type \'3\' to run away!. \n",0.5)
    fight_input = int(input("\nWhat do you want to do? : "))
    if fight_input == 1:

        monster_health = all_monsters[input_for_fight].health
        monster_damage = all_monsters[input_for_fight].damage
        new_health_monster = monster_health
        new_player_health = new_character.health

        while new_health_monster > 0 and new_player_health > 0:

            print_and_sleep(f"\nThe {selected_monster}'s health is {new_health_monster}", 2)
            print_and_sleep(f"\nYour health is {new_player_health} \n", 2)
            damage_done_with_hit = random.randint(0,new_character.damage)
            

            if new_player_health > 0 and new_health_monster > 0:
                if damage_done_with_hit < new_health_monster:
                    new_health_monster = new_health_monster - damage_done_with_hit
                    print_and_sleep(f"You hit the {selected_monster} and take {damage_done_with_hit} of his health with your attack! his health is now {new_health_monster} but he will attack you now!",3)
                else:
                    print_and_sleep(f"You hit the {selected_monster} with a {damage_done_with_hit} and take his last health with your attack! his health is now 0 and he dies in front of your eyes",3)
                    new_health_monster = 0

            damage_done_by_monster = random.randint(0,monster_damage)
            




            if new_health_monster > 0 and new_player_health > 0:
                if damage_done_by_monster < new_player_health:
                    new_player_health = new_player_health - damage_done_by_monster
                    print_and_sleep(f"\nThe {selected_monster} hits back! He hits a {damage_done_by_monster} and your health is now {new_player_health} but it's your turn to fight now!",3)
                else:
                    print_and_sleep(f"The {selected_monster} hits a {damage_done_by_monster} and it kills you.. I told you you wouldn\'t last.....",3)        
                    new_player_health = 0



            if new_player_health <= 0:
                print_and_sleep("YOU DIED!!!!!!!",1)
                print_and_sleep("YOU DIED!!!!!!!",1)
                print_and_sleep("YOU DIED!!!!!!!",1)
                print_and_sleep("YOU DIED!!!!!!!",1)
                #loss()
                continue_adventure()
            elif new_health_monster <= 0:
                print_and_sleep(f"\nYou killed the {selected_monster}!!! ",1)
                win(monster_health, selected_monster)
                continue_adventure()


    elif fight_input == 2:
        print(f"\nnot available yet, sorry!")
        continue_adventure()
    elif fight_input == 3:
        print("\nYou ran away!! coward.....")
        continue_adventure()
    else:
        fight()



#Check experience and checks if you level up
def check_level(check_exp):
    if new_character.experience < 83:
        new_character.level = 1
    elif new_character.experience > 82 and new_character.experience < 140:
        new_character.level = 2
    elif new_character.experience > 139 and new_character.experience < 200:
        new_character.level = 3
    elif new_character.experience > 199 and new_character < 300:
        new_character.level = 4
    else:
        new_character.level = 5
    return new_character.level


#Granting EXP / GOLD For a kill!
def win(monster_health, selected_monster):  
    gained_exp = monster_health * 4
    gained_gold = monster_health * 2
    new_character.experience = new_character.experience + gained_exp
    new_character.gold = new_character.gold + gained_gold
    print_and_sleep(f"\nCongratulations on killing the {selected_monster}! You gained {gained_exp} exp and you gained {gained_gold} coins.  \n",2)
    print_and_sleep(f"Your total balance of coins is now {new_character.gold}\n",2)
    check_exp = new_character.experience
    check_level(check_exp)
    print_and_sleep(f"Your total experience is now {new_character.experience} and your level is {new_character.level}!",1)
    return new_character.experience, new_character.gold






# nog niks aan gedaan
def play_game():
    introduction()
    weapon_store()


