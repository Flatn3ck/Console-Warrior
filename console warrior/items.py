from classes import Character, Weapon, Armour, Monster


all_weapons = [
  Weapon(name = 'Wooden Knuckle Duster', price = 5, damage = 3),
  Weapon(name = 'Wooden Sword', price = 10, damage = 5),
  Weapon(name = 'Iron Dagger', price = 35, damage = 7),
  Weapon(name = 'Iron Sword', price = 75, damage = 9),
  Weapon(name = 'Iron Machete', price = 85, damage = 11),
  Weapon(name = 'Steel Longsword', price = 125, damage = 16),
  Weapon(name = 'Steel Mace', price = 250, damage = 25),
  Weapon(name = 'Ray Gun', price = 2147483647, damage = 15000),
  Weapon(name = 'Lange Dildo', price = 2147483647, damage = 15000)
]



all_armour = [
  Armour(name ='Leather Sandals', price = 5, defence = 3),
  Armour(name ='Leather Shield', price = 10, defence = 5),
  Armour(name ='Leather Body ', price = 35, defence = 7),
  Armour(name ='Tinfoil Hat', price = 75, defence = 9),
  Armour(name ='Amulet of the Gaylords', price = 125, defence = 10),
  Armour(name ='Steel Skirt', price = 125, defence = 13),
  Armour(name ='Grandmaster Shield', price = 500, defence = 25),
  Armour(name ='Grandmaster Helmet', price = 750, defence = 40),
  Armour(name ='Grandmaster Tassets', price = 1000, defence = 55),
  Armour(name ='Grandmaster Hauberk', price = 1500, defence = 80),
  Armour(name ='Gucci Flip-flops', price = 2147483647, defence = 15000)
]


all_monsters = [
  Monster(name ='Rat', health = 3, armor = 0, damage = 1, level = 1),
  Monster(name ='Zombie', health = 10, armor = 0, damage = 3, level = 4),
  Monster(name ='Armoured Zombie', health = 25, armor = 5, damage = 5, level = 15)
]



