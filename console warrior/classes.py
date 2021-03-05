class Character:
  def __init__(self, health, armor, damage, level, gold, experience, weapon, gear):
    self.health = health
    self.armor = armor
    self.damage = damage
    self.level = level
    self.gold = gold
    self.experience = experience
    self.weapon = "Fists"
    self.gear = "Underwear"
new_character = Character(10, 0, 1, 1, 25, 0, "Fists", "Underwear")                                     

class Weapon:
    def __init__(self, name, price, damage):
        self.name = name
        self.price = price
        self.damage = damage

class Armour:
    def __init__(self, name, price, defence):
        self.name = name
        self.price = price
        self.defence = defence

class Monster:
  def __init__(self, name,  health, armor, damage, level):
    self.name = name
    self.health = health
    self.armor = armor
    self.damage = damage
    self.level = level


