class Player(object):
	def __init__(self, title, attack1, attack2, attack3):
		self.title = title
		self.attackname1 = attackname1
		self.attackname2 = attackname2
		self.attackname3 = attackname3
		self.attackpower1 = attackpower1
		self.attackpower2 = attackpower2
		self.attackpower3 = attackpower3

player_wizard = Player("Wizard", "a magic missile", "ray of frost", "lightning", 1, 3, 5)
player_fighter = Player("Fighter", "slashes at", "stabs", "hacks a piece off of", 1, 3, 5)
player_rogue = Player("Rogue", "poison darts", "backstabs", "garrotes", 1, 3, 5)
player_cleric = Player("Cleric", "shadow aura", "a psyche bolt", "soul drain", 1, 3, 5)
player_ranger = Player("Ranger", "an arrow", "stabs", "a fire arrow", 1, 3, 5)
