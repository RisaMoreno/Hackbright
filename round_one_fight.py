import players
import monsters1
from random import choice

playerhp = 20
monsterhp = 20

playerdeath = False
monsterdeath = False

pc = raw_input("What character do you want to play? \n Cleric \n Fighter \n Ranger \n Rogue \n Wizard")
  
player1 = players.Player(pc)
#player_wizard = Player("Wizard", "a magic missile", "ray of frost", "lightning", 1, 3, 5)
  
#pull player info from player class
#pull random monster to fight
fightingmonster = choice(Monster)

#player turn - choose your attack
playerattack = raw_input(pc "choose your attack!" attack1 attack2 attack3)
#enter key
#key = playerattack
#attack_chosen = player.attacks[key-1] ---> this should give you {"a magic missile":1}
#print attack_chosen.keys()  --->that should get you "a magic missile"
#print attack_chosen.get("a magic missile") --> 1

#monster turn - random attack key
#key = monsterattack

print "You attack " fightingmonster "with " """attack""" "for " """attackvalue""" damage. Ouch!"
  
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


    
def __main__:
  
    
if __name__ = "__main__":
  main()
