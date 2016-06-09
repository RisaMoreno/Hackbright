import players
import monsters1

playerhp = 10
monsterhp = 10

playerdeath = False
monsterdeath = False

while playerhp > 0:
  if playerhp <= 0:
    playerdeath = True
  else:
    #keep playing
if(playerdeath):
  print "You have died! Play again y/n?"

while monsterhp > 0:
  if monsterhp <= 0:
    monsterdeath = True
  else:
    #keep playing
if(monsterdeath):
  print "You have slain the beast! All hail! Play again y/n?"
