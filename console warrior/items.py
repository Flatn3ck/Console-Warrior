from classes import *


all_weapons = [
  Weapon(name = 'Wooden Knuckle Duster', price = 5, damage = 3),
  Weapon(name = 'Wooden Sword', price = 10, damage = 5),
  Weapon(name = 'Iron Dagger', price = 35, damage = 7),
  Weapon(name = 'Iron Sword', price = 75, damage = 9),
  Weapon(name = 'Iron Machete', price = 85, damage = 11),
  Weapon(name = 'Steel Longsword', price = 125, damage = 16),
  Weapon(name = 'Steel Mace', price = 250, damage = 25),
  Weapon(name = 'Ray Gun', price = 2147483647, damage = 15000),
  Weapon(name = 'Nuclear Bomb', price = 2147483647, damage = 15000)
]



all_armour = [
  Armour(name ='Leather Sandals', price = 5, defence = 3, hpboost = 5),
  Armour(name ='Leather Shield', price = 10, defence = 5, hpboost = 10),
  Armour(name ='Leather Body ', price = 35, defence = 7, hpboost = 15),
  Armour(name ='Tinfoil Hat', price = 75, defence = 9, hpboost = 20),
  Armour(name ='Amulet of the Gaylords', price = 125, defence = 10, hpboost = 25),
  Armour(name ='Steel Skirt', price = 125, defence = 13, hpboost = 30),
  Armour(name ='Grandmaster Shield', price = 500, defence = 25, hpboost = 35),
  Armour(name ='Grandmaster Helmet', price = 750, defence = 40, hpboost = 40),
  Armour(name ='Grandmaster Tassets', price = 1000, defence = 55, hpboost = 45),
  Armour(name ='Grandmaster Hauberk', price = 1500, defence = 80, hpboost = 50),
  Armour(name ='Gucci Flip-flops', price = 2147483647, defence = 15000, hpboost = 666)
]


all_monsters = [
  Monster(name ='Rat', health = 7, armor = 0, damage = 2, level = 1),
  Monster(name ='Zombie', health = 10, armor = 0, damage = 4, level = 4),
  Monster(name ='Vampire', health = 15, armor = 3, damage = 5, level = 9),
  Monster(name ='Werewolf', health = 25, armor = 5, damage = 8, level = 15),
  Monster(name ='Armoured Zombie', health = 28, armor = 10, damage = 15, level = 18),
  Monster(name ='Gnome Child', health = 50, armor = 15, damage = 20, level = 28),
  Monster(name ='Senpei', health = 666, armor = 666, damage = 666, level = 666)
]


all_bosses = [
  Boss(name = '', health = 50, armor = 20, damage = 25, level = 30)
]
