class Monster(object):
	def __init__(self, name):
		self.name = name
		self.monsterattack={"claws you":1, "bites you":3, "takes a bite out of you":5}
		
monster_hellhound = Monster("Hellhound")
monster_wendigo = Monster("Wendigo")
monster_hexenwulf = Monster("Hexenwulf")
monster_dragon = Monster("Dragon")
monster_gryphon = Monster("Gryphon")

monsterhp = 20

monsterdeath = False

from random import choice

choice(Monster)

def monster_damage(monsterhp):
  global monsterhp
  monsterhp = monsterhp - playerattack
  return monsterhp
  while monsterhp > 0:
    if monsterhp <= 0:
      monsterdeath = True
    else:
      #loop through player turn
  if(monsterdeath):
    end = raw_input("You have slain the beast! All hail! Play again y/n?" )
    if end="n":
      quit()
    else:
      #play again
