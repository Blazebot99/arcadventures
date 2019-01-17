import time
from Enemies import Enemy

def ability_selector(player):
  '''
  Ability selector menu.

  Based on the class chosen by the player.

  Parameters
  ----------
  player: Player()
    The player of the game.

  Returns
  -------
  None
  '''
  if len(player.classAbilities)==0:
    return
  chosen=False
  while not chosen:
    for i in range(len(player.classAbilities)):
      print(str(i+1)+":", player.classAbilities[i].name)
      print("Cost:", player.classAbilities[i].cost)
      print(player.classAbilities[i].desc)
    try:
      choice=int(input("Enter number of ability you wish to learn."))
      if choice<1 or choice>len(player.classAbilities):
        print("Please pick a valid number."+"\n")
      else:
        chosen=True
        player.learn_ability(choice-1)
    except:
      print("Please enter an integer value."+ "\n")

def stat_adder(player, points):
  '''
  The overworld function for the game.

  Contains various nested while loops to construct the layers of menus, different interfaces for when the player is in a town and when they are not.

  Parameters
  ----------
  player: Player()
    The player of the game.

  points: int
    The amount of points the player has to spend on stats.

  Returns
  -------
  None
  '''
  while points>0:
    print( "\n"+ "Points left:", points)
    print("HP:", player.maxhp)
    print("MP:", player.maxmp)
    print("Attack:", player.patk)
    print("Defense:", player.pdef)
    print("Magic Attack:", player.matk)
    print("Magic Defense:", player.mdef)
    print("Speed:", player.spd)
    stat=input("Choose stat to invest into.")
    if stat.lower()=="attack" or stat.lower()=="atk":
      points-=1
      player.patk+=1
      player.currentatk+=1
    elif stat.lower()=="defense" or stat.lower()=="def":
      points-=1
      player.pdef+=1
      player.currentdef+=1
    elif stat.lower()=="magic attack" or stat.lower()=="matk":
      points-=1
      player.matk+=1
      player.currentmatk+=1
    elif stat.lower()=="magic defense" or stat.lower()=="mdef":
      points-=1
      player.mdef+=1
      player.currentmdef+=1
    elif stat.lower()=="speed" or stat.lower()=="spd":
      points-=1
      player.spd+=1
      player.currentspd+=1
    elif stat.lower()=="hp":
      points-=1
      player.maxhp+=1
      player.currenthp+=1
    elif stat.lower()=="mp":
      points-=1
      player.maxmp+=1
      player.currentmp+=1
    else:
      print("Invalid stat.")
      
def battle_menu(player, enemylist, order):
  import random
  while True:
    print("Your turn.")
    print("HP: " + str(player.currenthp) + "/" + str(player.maxhp))
    print("MP: " + str(player.currentmp) + "/" + str(player.maxmp))
    print("Attack")
    print("Defend")
    print("Use Ability")
    print("Use Item")
    action=input("Choose action.")
    if action.lower()=="attack":
      enemyIndex=0
      for enemy in enemylist:
        print(str(enemyIndex+1)+":", enemy.name)
        enemyIndex+=1
      try:
        target=int(input("Choose number of enemy to attack."))
        if target < 1 or target > len(enemylist):
          print("Please enter a valid number.")
        else:
          enemy=enemylist[target-1]
          player.attack(enemy)
          if enemy.currenthp<=0:
            del enemylist[target-1]
            print(enemy.name + " down!")
          return
      except:
        print("Please enter an integer.")
    elif action.lower()=="defend":
      player.currentdef+=int(player.pdef*1.1)
      player.currentmdef+=int(player.mdef*1.1)
      return
    elif action.lower()=="use item":
      print("\n"+ "Inventory")
      for item in player.inventory:
        print(item.name)
        print(item.desc)  
      name=input("Choose item to use.")
      if name.lower() in player.itemNames:
        item=player.inventory[player.itemNames.index(name.lower())]
        player.use_battle_item(item)
        return
      else:
        print("You don't possess that item or it does not exist.") 
    elif action.lower()=="use ability":
      for ability in player.chosenAbilities:
        print(ability.name, "Cost: " + str(ability.cost) + " MP")
        print(ability.desc)
      use=input("Choose ability to use.")
      if use.lower()=="guard break":
        if player.currentmp<3:
          print("Not enough MP!")
        else:
          enemyIndex=0
          for enemy in enemylist:
            print(str(enemyIndex+1)+":", enemy.name)
            enemyIndex+=1
          target=int(input("Choose number of enemy to attack."))
          if target < 1 or target > len(enemylist):
            print("Please enter a valid number.")
          else:
            enemy=enemylist[target-1]
            player.attack(enemy)
          if enemy.currenthp<=0:
            del enemylist[target-1]
            print(enemy.name + " down!")
          else:
            print(enemy.name + "'s defense was lowered!")
            enemy.currentdef=int(enemy.currentdef*0.75)
          player.currentmp-=3
          return
      elif use.lower()=="whirlwind strike":
        if player.currentmp<7:
          print("Not enough MP!")
        else:
          enemyIndex=0
          for enemy in enemylist:
            player.attack(enemy)
            if enemy.currenthp<=0:
              del enemylist[enemyIndex]
              print(enemy.name + " down!")
            enemyIndex+=1
          player.currentmp-=7
          return
      elif use.lower()=="feint":
        if player.currentmp<4:
          print("Not enough MP!")
        else:
          enemyIndex=0
          for enemy in enemylist:
            print(str(enemyIndex+1)+":", enemy.name)
          enemyIndex+=1
          target=int(input("Choose number of enemy to attack."))
          if target < 1 or target > len(enemylist):
            print("Please enter a valid number.")
          else:
            enemy=enemylist[target-1]
            enemy.currentspd=int(enemy.currentspd*0.75)
            print(enemy.name + "'s speed was lowered!")
            player.currentmp-=4
            return
      elif use.lower()=="snipe":
        if player.currentmp<4:
          print("Not enough MP!")
        else:
          enemyIndex=0
          for enemy in enemylist:
            print(str(enemyIndex+1)+":", enemy.name)
            enemyIndex+=1
          target=int(input("Choose number of enemy to attack."))
          if target < 1 or target > len(enemylist):
            print("Please enter a valid number.")
          else:
            enemy=enemylist[target-1]
            rng=random.Random()
            crit=rng.randint(0, 1)
            if crit==0:
              player.attack(enemy)
            else:
              print(player.name + " attacks!")
              if player.weapon.aT=="Physical":
                damage=player.currentatk-target.currentdef
              elif player.weapon.aT=="Magical":
                damage=player.currentmatk-target.currentmdef
              target.currenthp-=damage*2
              print("Critical Hit!")
              print("Dealt "+ str(damage) + " damage to " + target.name +"!")
              if enemy.currenthp<=0:
                del enemylist[target-1]
                print(enemy.name+ " down!")
              player.currentmp-=4
              return
      elif use.lower()=="camouflage":
        if player.currentmp<3:
          print("Not enough MP!")
        else:
          print("Speed increased!")
          player.spd*=1.2
          player.currentmp-=4
          return
      elif use.lower()=="multishot":
        if player.currentmp<7:
          print("Not enough MP!")
        else:
          enemyIndex=0
          for enemy in enemylist:
            print(str(enemyIndex+1)+":", enemy.name)
            enemyIndex+=1
          target=int(input("Choose number of enemy to attack."))
          if target < 1 or target > len(enemylist):
            print("Please enter a valid number.")
          else:
            enemy=enemylist[target-1]
            player.attack(enemy)
            player.attack(enemy)
            if enemy.currenthp<=0:
              del enemylist[target-1]
              print(enemy.name + " down!")
            player.currentmp-=7
          return
      elif use.lower()=="ring of magic":
        if player.currentmp<5:
          print("Not enough MP!")
        else:
          print("Magic attack boosted!")
          player.currentmatk=int(player.currentmatk*1.2)
          player.currentmp-=5
          return
      elif use.lower()=="prism shock":
        if player.currentmp<3:
          print("Not enough MP!")
        else:
          enemyIndex=0
          for enemy in enemylist:
            print(str(enemyIndex+1)+":", enemy.name)
            enemyIndex+=1
          target=int(input("Choose number of enemy to attack."))
          if target < 1 or target > len(enemylist):
            print("Please enter a valid number.")
          else:
            enemy=enemylist[target-1]
            print(player.name + " attacks!")
            if player.weapon.aT=="Physical":
              damage=player.currentatk-enemy.currentdef
            elif player.weapon.aT=="Magical":
              damage=player.currentmatk-enemy.currentdef
            enemy.currenthp-=damage
            print("Dealt "+ str(damage) + " damage to " + enemy.name +"!")
            if enemy.currenthp<=0:
              del enemylist[target-1]
              print(enemy.name + " down!")
            player.currentmp-=3
            return
      elif use.lower()=="tri-elemental":
        if player.currentmp<10:
          print("Not enough MP!")
        else:
          enemyIndex=0
          for enemy in enemylist:
            print(str(enemyIndex+1)+":", enemy.name)
            enemyIndex+=1
          target=int(input("Choose number of enemy to attack."))
          if target < 1 or target > len(enemylist):
            print("Please enter a valid number.")
          else:
            enemy=enemylist[target-1]
            player.attack(enemy)
            player.attack(enemy)
            player.attack(enemy)
            if enemy.currenthp<=0:
              del enemylist[target-1]
              print(enemy.name + " down!")
            player.currentmp-=10
            return
      else:
        print("Ability does not exist or you do not have access to it.")
    else:
      print("Invalid action.")

def battle_loop(player, enemylist):
  '''
  The battle system for the game.

  Includes all the possible abilities the player could use.
  Parameters
  ----------
  player: Player()
    The player of the game.

  enemylist: list
    The list of all enemies to defeat.
    
  Returns
  -------
  None
  '''
  print("Enemies appear!")
  time.sleep(1)
  for enemy in enemylist:
    print(enemy.name)
  time.sleep(1)
  #make a copy to be used to calculated exp and gold at the end if victorious
  copy=enemylist.copy()
  combatants=enemylist
  #While player is not defeated and not all enemies are down, keep the battle going.
  Turn=1
  while player.currenthp>0 and len(combatants)>0:
    #sift the player into the list to be sorted
    combatants.append(player)
    #Sort the combatants by speed, from slowest to quickest
    combatants.sort()
    #Reverse it so that it's in order from quickest to slowest
    combatants=combatants[::-1]
    #set a copy of the list
    battle_order=combatants.copy()
    #reset the combatants to include only the enemies
    print(battle_order)
    combatants=enemylist
    combatants.remove(player)
    print("Turn " + str(Turn))
    Turn+=1
    #resets player's turn confirmation
    player.moved=False
    for combatant in battle_order:
      print(combatant.name)
      if type(combatant)==type(Enemy("Test Dummy")) and combatant in combatants:
        combatant.attack(player)
        if player.currenthp<=0:
          break
      elif player.moved==False:
        battle_menu(player, combatants, battle_order)
        player.moved=True
  if player.chosenOne is True:
    player.currentatk=player.patk+player.weapon.pdmg+player.secondWeapon.pdmg
    player.currentdef=player.pdef+player.armor.pdef
    player.currentmatk=player.matk+player.weapon.mdmg+player.secondWeapon.mdmg
    player.currentmdef=player.mdef+player.armor.pdef
    player.currentspd=player.spd+player.armor.spd+player.weapon.spd
  else:
    player.currentatk=player.patk+player.weapon.pdmg+player.armor.pdmg
    player.currentdef=player.pdef+player.weapon.pdef+player.armor.pdef
    player.currentmatk=player.matk+player.weapon.mdmg+player.armor.mdmg
    player.currentmdef=player.mdef+player.weapon.pdef+player.armor.pdef
    player.currentspd=player.spd+player.armor.spd+player.weapon.spd+player.armor.spd
  if player.currenthp<=0:
    print("You were defeated...")
    player.location=player.recentTown
    player.gold=int(player.gold/2)
    player.currenthp=player.maxhp
    player.currentmp=player.maxmp
  else:
    print("You were victorious!")
    total=0
    for enemy in copy:
      total+=enemy.spd
    average=int(total/len(copy))
    print("Acquired " + str(average) + " gold.")
    player.gold+=average
