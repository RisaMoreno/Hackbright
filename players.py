class Player(object):
	def __init__(self, title):
		self.title = title
		if self.title == Wizard:
			attacks = [{"casts a magic missile":1}, {"casts ray of frost":3}, {"casts lightning":5}]
		if self.title == Fighter:
			attacks = [{"slashes at":1}, {"stabs":3}, {"hacks a piece off of":5,}]
		if self.title == Rogue:
			attacks = [{"poison darts":1}, {"backstabs":3}, {"garrotes":5,}]
		if self.title == Cleric:
			attacks = [{"uses shadow aura":1}, {"casts psyche bolt":3}, {"uses soul drain":5}]
		if self.title == Ranger:
			attacks = [{"fires an arrow":1}, {"stabs":3}, {"a fire arrow":5}]

player_wizard = Player("Wizard")
player_fighter = Player("Fighter")
player_rogue = Player("Rogue")
player_cleric = Player("Cleric")
player_ranger = Player("Ranger")

def player_damage(playerhp):
  global playerhp
  playerhp = playerhp - monsterattack
  return playerhp
  while playerhp > 0:
    if playerhp <= 0:
      playerdeath = True
    else:
      #loop through monster turn
  if(playerdeath):
    end = raw_input("You have died! Play again y/n? ")
    if end="n":
      quit()
    else:
      #play again
      
 player_wizard = Player("Wizard")
 
 #test in class file!
      
 print player_wizard = Player("Wizard")
 
 
