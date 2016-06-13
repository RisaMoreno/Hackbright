import players
import monsters1

playerhp = 20
monsterhp = 20

playerdeath = False
monsterdeath = False

pc = raw_input("What character do you want to play? \n Cleric \n Fighter \n Ranger \n Rogue \n Wizard")
  

  
def monster_damage(monsterhp):
  global monsterhp
  monsterhp = monsterhp - #playerattack
  return monsterhp

def player_damage(playerhp):
  global playerhp
  playerhp = playerhp - #monsterattack
  return playerhp

while playerhp > 0:
  if playerhp <= 0:
    playerdeath = True
  else:
    #keep playing
if(playerdeath):
  end = raw_input("You have died! Play again y/n? ")
  if end="n":
  quit()
  else:
    #play again

while monsterhp > 0:
  if monsterhp <= 0:
    monsterdeath = True
  else:
    #keep playing
if(monsterdeath):
  end = raw_input("You have slain the beast! All hail! Play again y/n?" )
  if end="n":
  quit()
  else:
    #play again
