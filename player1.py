class Player(object):
	def __init__(self, title):
		self.title = title
		if self.title == "Wizard":
			attack_wizard = [{"casts a magic missile":1}, {"casts ray of frost":3}, {"casts lightning":5}]
		if self.title == "Fighter":
			attack_fighter = [{"slashes at":1}, {"stabs":3}, {"hacks a piece off of":5,}]
		if self.title == "Rogue":
			attack_rogue = [{"poison darts":1}, {"backstabs":3}, {"garrotes":5,}]
		if self.title == "Cleric":
			attack_cleric = [{"uses shadow aura":1}, {"casts psyche bolt":3}, {"uses soul drain":5}]
		if self.title == "Ranger":
			attack_ranger = [{"fires an arrow":1}, {"stabs":3}, {"a fire arrow":5}]

player_wizard = Player("Wizard")
player_fighter = Player("Fighter")
player_rogue = Player("Rogue")
player_cleric = Player("Cleric")
player_ranger = Player("Ranger")

player_hp = 20

player_death = False

def player_attack():
	player_attack = raw_input(pc "choose your attack!" player1.title attack1 attack2 attack3)

def player_damage(player_hp):
    #global playerhp
    player_hp = player_hp - monster_attack
    
    while player_hp > 0:
    # print fightingmonster """attack""" pc "for " """attackvalue""" damage. Ouch!"
        if player_hp <= 0:
            player_death = True
        else:
        	turn_count += 1
        	print "Monster's turn!"
  			#loop through monster turn
    if(player_death):
        end = raw_input("You have died! Play again y/n? ")
    	if end == "n":
        	quit()
    	else:
        	print "Play again!"
    			#play again

player_wizard = Player("Wizard")
 
 #test in class file!
print player_wizard.title == Player("Wizard").title
print player_wizard
print Player("Wizard")
