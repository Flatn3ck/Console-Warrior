from classes import Character, Weapon, Armour, Monster, new_character
from items import all_weapons, all_monsters, all_armour

# asks for player name, tells player his current stats + coins 
def introduction():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("~~~~~~~~~~Welcome to Console Warrior~~~~~~~~~~\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    character_name = input("What is your character\'s name? : ")

    print(f"\nWelcome {character_name}! Your current stats are : \n")
    stats()
    print("\nLet\'s head over to the shop! We can buy weapons and armour there.")
    return character_name
    weapon_store()

def stats():
    print(f"******************")
    print(f"**   Level: {new_character.level}   **")
    print(f"**  Health: {new_character.health}  **")
    print(f"**   Armor: {new_character.armor}   **")
    print(f"**   Gold: {new_character.gold}   **")
    print(f"******************\n")
    print(f"Your current weapon is: {new_character.weapon}")
    print(f"Your current armour is: {new_character.gear}")








# elke keer dat je wapens / armour wilt kopen deze functie uitvoeren
def weapon_store():
    print("\nWelcome to the weapon store of Console Warrior\n")
    while True:
        try:
            the_input = int(input(f"- Type \'1\' to see the weaponshop  \n- Type \'2\' to see the armourshop \n- Type \'3\' to start playing. \n\nDon\'t start playing with no gear, you\'ll die. : "))
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
                    print(f"\nThe weapon you selected is {selected_weapon} and it costs {selected_weapon_price} coins \n")
                    answer = input("if you want to buy this item type \'yes\' : ")

                    if answer == 'yes' and new_character.gold >= selected_weapon_price :  
                        new_character.gold = new_character.gold - selected_weapon_price
                        new_character.weapon = selected_weapon                                              
                        print(f"\nYou bought a {selected_weapon} and you have {new_character.gold} coins left.\n")
                        weapon_store()
                        return new_character.weapon, new_character.gold
                        
                    elif answer == 'yes' and new_character.gold < selected_weapon_price:
                        print(f"\nYou don\'t have enough money to purchase {selected_weapon}")
                    else:
                        print("\nType \'yes\' to buy it.")

######################################################################################################################################################################
        elif the_input == 2:
            print("\n      ~~~~~ARMOUR SHOP~~~~~             \n")
            print("__________________________________\n")
            # This will loop through the armours and displays them
            for i, armour in enumerate(all_armour):
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
                    selected_armour_price = all_armour[input_for_armour].price
                    print(f"\nThe armour you selected is {selected_armour} and it costs {selected_armour_price} coins \n")
                    answer = input("if you want to buy this item type \'yes\' : ")

                    if answer == 'yes' and new_character.gold >= selected_armour_price :  
                        new_character.gold = new_character.gold - selected_armour_price
                        new_character.gear = selected_armour                                              
                        print(f"\nYou bought a {selected_armour} and you have {new_character.gold} coins left.\n")
                        break
                    elif answer == 'yes' and new_character.gold < selected_armour_price:
                        print(f"\nYou don\'t have enough money to purchase {selected_armour}")
                    else:
                        print("\nType \'yes\' to buy it.")

######################################################################################################################################################################
        elif the_input == 3:
            print("\nSTART OF THE ADVENTURE\n")
            stats()
            print("\nSHOW OPTIONS\n")
            break


        else:
            print("1, 2 or 3 man don\'t be retarded")




# nog niks aan gedaan
def play_game():
    introduction()
    weapon_store()