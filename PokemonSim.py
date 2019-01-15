import pygame
import random
import time
pname 1 = input("What is the first Trainer's name?")
pname 2 = input("And what is the second Trainer's name?")
print(f"Welcome, {pname1} and {pname2}, to Pokemon Battle Simulator, Super Special Python Edition! You will be prompted shortly to choose your team of 3 Pokemon, each with a competitively viable moveset and setup.")
time.sleep(5)
class Pokemon:
    def __init__(self, level, ability, nature, type,type2, item, hpmax, hpcurrent, atk, defs, spatk, spdef,spd, moves, status)
    self.name = name
    self.level = level
    self.ability = ability
    self.nature = nature
    self.type = type
    self.type2 = type2
    self.item = item
    self.hpmax = hpmax
    self.hpcurrent = hpcurrent
    self.atk = atk
    self.defs = defs
    self.spatk = spatk
    self.spdef = spdef
    self.spd = spd
    self.moves = moves
    self.status = status
def damage():
  if move.atktype = phys:
    damagephys = ((((((((42)*chosenmove.power)*(self.atk/opponent.defs))/50)+2)*random.randuniform(.88,1.12))
    if self.status = brn:
      x = damagephys/2
  elif move.atktype = spec:
   x = ((((((((42)*chosenmove.power)*(self.spatk/opponent.spdef))/50)+2)*random.randuniform(.88,1.12))
  else:
    dmg = 0
def battleaction():
  x = input("Would you like to use a (M)ove or    (S)witch pokemon?")
  if x = M:
    y = input(f"What move would you like to use? You can pick from {self.moves}")
  elif x = S:
    z = input("Which Pokemon would you like to switch to?")
    self = z
  else:
    print("Type either M or S, to use a (M)ove or (S)witch.")
    battleaction()
self = input("Which Pokemon would you like to send out first?")
opponent = input("Other Player, which Pokemon would you like to send out?")
def battle(self, opponent):
  while self.hpcurrent and opponent.hpcurrent >0:
    if self.spd > opponent.spd:
      battleaction(self)
    elif opponent.spd > self.spd:
      battleaction(opponent)
Ability_List = {name: effect}
Move_List = {name: Type, Dmg_Type, Power, Effect}
Nature_List = {name: effect}

self, level, ability, nature, type,type2, item, hpmax, hpcurrent, atk, defs, spatk, spdef,spd, moves, status)

Venusaur = Pokemon('Venusaur', 100, 'Chlorophyll', 'modest', 'Grass', 'Poison', 'Life Orb', 220, 220, 164, 168, 326, 200, 286, 'Growth' 'Sludge Bomb' 'Giga Drain' 'Hidden Power Fire', NONE)
Charizard = Pokemon('Charizard', 100, 'Solar Power', 'modest', 'Fire', 'Flying', 'Choice Specs', 216, 216, 168, 156, 218, 172, 326, 'Fire Blast' 'Solar Beam' 'Focus Blast' 'Flamethrower', NONE)
Blastoise = Pokemon('Blastoise', 100, 'Rain Dish', 'modest', 'Water', 'Water', 'Blastoisinite', 218, 218, 292, 200, 218, 172, 326, 'Fire Blast' 'Solar Beam' 'Focus Blast' 'Flamethrower', NONE)


}

