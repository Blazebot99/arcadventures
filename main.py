#-----------------------------------------------------------------------------
# Name:        <Adventures In Arcadia> (ArcAdventure.py)
# Purpose:     <A simple text-based game.>
#
# Author:      <Jason Tian>
# Created:     <November 1, 2018>
# Updated:     <November 11, 2018>
#------------------------------------------------------------------------------
import time
from Classes import *
from Functions import *
from Storyline import *

def overworld(player):
  '''
  The overworld function for the game.

  Contains various nested while loops to construct the layers of menus, different interfaces for when the player is in a town and when they are not.

  Parameters
  ----------
  player: Player()
    The player of the game.

  Returns
  -------
  None
  '''
  
  while True:
    print("\n" + "You are currently in " + player.location.name + ".")
    #If player is in a town
    if type(player.location)==Town:
      print("Actions:")
      print("Move")
      print("Shop")
      print("Inn")
      print("Menu")
      print("Quit Game")
      choice=input("Choose an action:")
      #Moving system
      if choice.lower()=="move":
        print("\n"+"Available locations:")
        for location in player.location.connections:
          print(location.name)
        print("")
        movement=input("Choose location to move to:")
        if movement.lower() in player.location.connectionNames:
          sure=input("Move to " + player.location.connections[player.location.connectionNames.index(movement.lower())].name + "?")
          if sure.lower()[0]=="y":
            player.location=player.location.connections[player.location.connectionNames.index(movement.lower())]
            if player.location.visited==False and type(player.location)!=type(player.recentTown):
              player.location.story_continue(player)
              if player.location.cleared==True:
                player.location.visited=True
              else:
                player.location=player.recentTown
        elif movement.lower()==player.location.name.lower():
          print("Already at this location!")
        else:
          print("No such location!")
      #player menu
      elif choice.lower()=="menu":
        while True:
          print("\n"+ "Player Menu")
          print("Inventory")
          print("Equipment")
          print("Check Stats")
          print("Exit to Overworld")
          menuOption=input("Choose an option.")
          if menuOption.lower()=="exit" or menuOption.lower()=="exit to overworld":
            break
          #inventory 
          elif menuOption.lower()=="inventory":
            while True:
              print("\n"+ "Inventory")
              if player.inventory==[]:
                print("You don't have any items.")
              for item in player.inventory:
                print(item.name)
                print(item.desc)  
              print("Use Item")
              print("Exit to Player Menu")
              choice=input("Choose action.")
              if choice.lower()=="use item":
                name=input("Choose item to use.")
                if name.lower() in player.itemNames:
                  item=player.inventory[player.itemNames.index(name.lower())]
                  player.use_item(item)
                else:
                  print("You don't possess that item or it does not exist.")
              elif choice.lower()=="exit" or choice.lower()=="exit to player menu":
                break
              else:
                print("Invalid Input.") 
          #equips menu       
          elif menuOption.lower()=="equipment":
            while True:
              print("\n"+"Equipment")
              if player.equipment==[]:
                print("You don't have any equipment on hand. ")
              for equip in player.equipment:
                print(equip.name, "Attack: " + str(equip.pdmg), "Defense: " + str(equip.pdef), "Magic Attack: " + str(equip.mdmg), "Magic Defense: " + str(equip.mdef), "Speed: " + str(equip.spd))
              print("Equip item")
              print("Exit to Player Menu")
              choice=input("Choose action.")
              if choice.lower()=="equip" or choice.lower()=="equip item":
                name=input("Choose item to equip.")
                if name.lower() in player.equipmentNames:
                  equip=player.equipment[player.equipmentNames.index(name.lower())]
                  choice=input("Equip " + equip.name + "?")
                  if choice.lower()[0]=="y":
                    if type(equip)==type(player.weapon):
                      player.equipWeapon(equip)
                    elif type(equip)==type(player.armor):
                      player.equipArmor(equip)
                else:
                  print("You don't have that equip, or it does not exist.")
              elif choice.lower()=="exit" or choice.lower()=="exit to player menu":
                break
              else:
                print("Invalid Input.")
          #check stats
          elif menuOption.lower()=="check stats":
            print("\n" + "Name:", player.name)
            print("HP:", str(player.currenthp) + "/" + str(player.maxhp))
            print("MP:", str(player.currentmp) + "/" + str(player.maxmp))
            print("\n"+ "Base Stats")
            print("Attack:", str(player.patk))
            print("Defense:", str(player.pdef))
            print("Magic Attack:", str(player.matk))
            print("Magic Defense:", str(player.mdef))
            print("Speed:", str(player.spd) + "\n")
            print("Current Stats")
            print("Attack:", str(player.currentatk))
            print("Defense:", str(player.currentdef))
            print("Magic Attack:", str(player.currentmatk))
            print("Magic Defense:", str(player.currentmdef))
            print("Speed:", str(player.currentspd)+"\n")
            print("Weapon:", player.weapon.name)
            if player.chosenOne==True:
              print("Second Weapon:", player.secondWeapon.name)
            print("Armor:", player.armor.name)
            if player.accessory is None:
              print("Accessory: None")
            else:
              print("Accessory:", player.accessory.name)
            print("Gold:", str(player.gold))
          else:
            print("Invalid Input.")
      #To the shop
      elif choice.lower()=="shop":
        print("Welcome to the shop!")
        while True:
          choice=input("What do you need, equipment or items? Or are you looking to sell?")
          if choice.lower()=="equipment":
            while True:
              print("\n")
              for equip in player.location.equipment:
                print(equip.name, "Cost: " + str(equip.cost) + " gold", "Attack: " + str(equip.pdmg), "Defense: " + str(equip.pdef), "Magic Attack: " + str(equip.mdmg), "Magic Defense: " + str(equip.mdef), "Speed: " + str(equip.spd))
              print("Your Gold: " + str(player.gold))
              choice=input("What're you looking to buy? Or did you want something else?")
              if choice.lower() in player.location.equipmentNames:
                equip=player.location.equipment[player.location.equipmentNames.index(choice.lower())]
                confirm=input("One " + equip.name + ", was it?")
                if confirm.lower()[0]=="y":
                  if player.gold<equip.cost:
                    print("You don't have enough money!")
                  else:
                    print("Purchased one " + equip.name + ".")
                    player.equipment.append(equip)
                    player.equipmentNames.append(equip.name.lower())
                    player.gold-=equip.cost
                  choice=input("Need any more equipment?")
                  if choice.lower()[0]!="y":
                    break
                else:
                  print("That's alright. Take your time.")
              elif choice.lower()=="else" or choice.lower()=="something else":
                break
              else:
                print("Sorry, we don't have that here!")
                choice=input("Need any more equipment?")
                if choice.lower()[0]!="y":
                  break
          elif choice.lower()=="items":
            while True:
              for item in player.location.items:
                print("\n"+ item.name, "Cost: " + str(item.cost) + " gold")
                print(item.desc)
              print("Your Gold: " + str(player.gold))
              choice=input("What're you looking to buy? Or have you changed your mind?")
              if choice.lower() in player.location.itemNames:
                item=player.location.items[player.location.itemNames.index(choice.lower())]
                confirm=input("One " + item.name + ", was it?")
                if confirm.lower()[0]=="y":
                  if player.gold<item.cost:
                    print("You don't have enough money!")
                  else:
                    print("Purchased one " + item.name + ".")
                    player.inventory.append(item)
                    player.itemNames.append(item.name.lower())
                    player.gold-=item.cost
                  choice=input("Need any more items?")
                  if choice.lower()[0]!="y":
                    break
                else:
                  print("That's alright. Take your time.")
              elif choice.lower()=="else" or choice.lower()=="something else":
                break
              else:
                print("Sorry, we don't have that here!")
                choice=input("Need any more items?")
                if choice.lower()[0]!="y":
                  break
          elif choice.lower()=="sell":
            while True:
              for equip in player.equipment:
                print(equip.name, "Value: " + str(int(equip.cost/2)) + " gold", "Attack: " + str(equip.pdmg), "Defense: " + str(equip.pdef), "Magic Attack: " + str(equip.mdmg), "Magic Defense: " + str(equip.mdef), "Speed: " + str(equip.spd))
              for item in player.inventory:
                  print(item.name, "Value: " + str(int(item.cost/2)) + " gold")
                  print(item.desc)
              print("Your Gold: " + str(player.gold))
              sell=input("So, what did you want to sell? Or did you want something else?")
              if sell.lower() in player.equipmentNames:
                equip=player.equipment[player.equipmentNames.index(sell.lower())]
                choice=input("So you're selling one " + equip.name + "? I'll pay you " + str(int(equip.cost/2))+" gold.")
                if choice.lower()[0]=="y":
                  print("You sold 1 " + equip.name + ".")
                  player.equipment.remove(equip)
                  player.equipmentNames.remove(equip.name.lower())
                  player.gold+=int(equip.cost/2)
                else:
                  print("That's alright, take your time.")
              elif sell.lower() in player.itemNames:
                item=player.inventory[player.itemNames.index(sell.lower())]
                choice=input("So you're selling one " + item.name + "? I'll pay you " + str(int(item.cost/2))+" gold.")
                if choice.lower()[0]=="y":
                  print("You sold 1 " + item.name + ".")
                  player.inventory.remove(item)
                  player.itemNames.remove(item.name.lower())
                  player.gold+=int(item.cost/2)
                  choice=input("Still selling?")
                  if choice.lower()[0]!="y":
                    break
                else:
                  print("That's alright, take your time.")
              elif choice.lower()=="else" or choice.lower()=="something else":
                  break
              else:
                print("Looks like you don't have that item.")
                choice=input("Still selling?")
                if choice.lower()[0]!="y":
                  break
          else:
            print("Sorry, I didn't quite catch that.")
          choice=input("Anything else?")
          if choice.lower()[0]!="y":
            break
      #inn menu
      elif choice.lower()=="inn":
        while True:
          print("\n" + "Welcome to the inn. It's 50 gold for a night here.")
          print("Stay the night")
          print("Exit to Overworld")
          choice=input("Choose action.")
          if choice.lower()=="stay the night":
            if player.gold < 50:
              print("You don't have enough money!")
            else:
              if player.currenthp==player.maxhp and player.currentmp==player.maxmp:
                print("You have no need to rest.")
              else:
                print("You wake up, and you feel refreshed.")
                player.currenthp=player.maxhp
                player.currentmp=player.maxmp
                player.gold-=round(player.gold*0.2)
          elif choice.lower()=="exit" or choice.lower()=="exit to overworld":
            break
          else:
            print("Invalid input.")
      elif choice.lower()=="quit game":
        quit=input("Quit game?")
        if quit.lower()[0]=="y":
          return
      else:
        print("Invalid action chosen.")
    #if the user is not at a town
    else:
      print("Actions:")
      print("Move")
      print("Menu")
      choice=input("Choose action.")
      if choice.lower()=="move":
        print("\n"+"Available locations:")
        for location in player.location.connections:
          print(location.name)
        print("")
        movement=input("Choose location to move to:")
        if movement.lower() in player.location.connectionNames:
          sure=input("Move to " + player.location.connections[player.location.connectionNames.index(movement.lower())].name + "?")
          if sure.lower()[0]=="y":
            player.location=player.location.connections[player.location.connectionNames.index(movement.lower())]
        elif movement.lower()==player.location.name.lower():
          print("Already at this location!")
        else:
          print("No such location!")
      elif choice.lower()=="menu":
        while True:
          print("\n"+ "Player Menu")
          print("Inventory")
          print("Equipment")
          print("Check Stats")
          print("Exit to Overworld")
          menuOption=input("Choose an option.")
          if menuOption.lower()=="exit" or menuOption.lower()=="exit to overworld":
            break
          elif menuOption.lower()=="inventory":
            while True:
              print("\n"+ "Inventory")
              if player.inventory==[]:
                print("You have no items available.")
              for item in player.inventory:
                print(item.name)
                print(item.desc)  
              print("Use Item")
              print("Exit to Player Menu")
              choice=input("Choose action.")
              if choice.lower()=="use item":
                  name=input("Choose item to use.")
                  if name.lower() in player.itemNames:
                    item=player.inventory[player.itemNames.index(name.lower())]
                    player.use_item(item)
                  else:
                    print("You don't possess that item or it does not exist.")
              elif choice.lower()=="exit" or choice.lower()=="exit to player menu":
                break
              else:
                print("Invalid Input.")        
          elif menuOption.lower()=="equipment":
            while True:
              print("\n"+"Equipment")
              if player.equipment==[]:
                print("You have no available equipment.")
              for equip in player.equipment:
                print(equip.name, "Attack: " + str(equip.pdmg), "Defense: " + str(equip.pdef), "Magic Attack: " + str(equip.mdmg), "Magic Defense: " + str(equip.mdef), "Speed: " + str(equip.spd))
              print("Equip item")
              print("Exit to Player Menu")
              choice=input("Choose action.")
              if choice.lower()=="equip" or choice.lower()=="equip item":
                name=input("Choose item to equip.")
                if name.lower() in player.equipmentNames:
                  equip=player.equipment[player.equipmentNames.index(name.lower())]
                  choice=input("Equip " + equip.name + "?")
                  if choice.lower()[0]=="y":
                    if type(equip)==type(player.weapon):
                      player.equipWeapon(equip)
                    elif type(equip)==type(player.armor):
                      player.equipArmor(equip)
                else:
                  print("You don't have that equip, or it does not exist.")
              elif choice.lower()=="exit" or choice.lower()=="exit to player menu":
                break
              else:
                print("Invalid Input.")
          elif menuOption.lower()=="check stats":
            print("\n" + "Name:", player.name)
            print("HP:", str(player.currenthp) + "/" + str(player.maxhp))
            print("MP:", str(player.currentmp) + "/" + str(player.maxmp))
            print("\n"+ "Base Stats")
            print("Attack:", str(player.patk))
            print("Defense:", str(player.pdef))
            print("Magic Attack:", str(player.matk))
            print("Magic Defense:", str(player.mdef))
            print("Speed:", str(player.spd) + "\n")
            print("Current Stats")
            print("Attack:", str(player.currentatk))
            print("Defense:", str(player.currentdef))
            print("Magic Attack:", str(player.currentmatk))
            print("Magic Defense:", str(player.currentmdef))
            print("Speed:", str(player.currentspd)+"\n")
            print("Weapon:", player.weapon.name)
            if player.chosenOne==True:
              print("Second Weapon:", player.secondWeapon.name)
            print("Armor:", player.armor.name)
            if player.accessory is None:
              print("Accessory: None")
            else:
              print("Accessory:", player.accessory.name)
            print("Gold:", str(player.gold))
          else:
            print("Invalid Input.")
      else:
        print("Invalid action chosen.")

def main():
  '''
  The function containing the game loop. 

  The bulk of this function is a while loop that keeps the game running until the user decides to quit. It includes various nested while loops to perform other functions. 

  Parameters
  ----------
  None

  Returns
  -------
  None
  '''
  while True:
    print("Adventures of Arcadia")
    print("Start Game")
    print("Close Game")
    choice=input("Type start to begin, or close to quit.")
    if choice.lower()=="start":
      print("\n" + "Welcome, aspiring adventurer." + "\n")
      print("This is the land of Arcadia, a realm where many evils dwelled, and where most were exterminated for good. However, it would seem one yet still lingers...perhaps the darkest of them all." + "\n")
      name=input("Tell me, what is your name?" + "\n")
      print("Ah, so your name is " + name + "." + "\n")
      passed=False
      background=input("Next...what is your background? A powerful warrior? Or A swift archer? Or perhaps a mage that controls the elements?" + "\n")
      while not passed: 
        if background.lower()=="warrior":
          passed=True
          player=Warrior(name)
          print("So you are a young upstart warrior who has decided to leave their town in seek of greater fortune." + "\n")
          print("And now, for your attributes. Of course, based on your background, you are naturally stronger in some areas than others. However, you still have potential power untapped...use it wisely.")
          #assert player.maxhp==35, "Incorrect HP value"
          stat_adder(player, 10)
        elif background.lower()=="archer":
          passed=True
          player=Archer(name)
          print("So you are a ranger-in-training who has been dispatched on a solo mission for the first time." + "\n")
          #assert player.spd=25, "Incorrect speed value"
          print("And now, for your attributes. Of course, based on your background, you are naturally stronger in some areas than others. However, you still have potential power untapped...use it wisely.")
          stat_adder(player, 10)
        elif background.lower()=="mage":
          passed=True
          player=Mage(name)
          print("Interesting...you are an acolyte on a journey to determine your true fate." + "\n")
          #assert player.matk=25, "Incorrect attack value"
          print("And now, for your attributes. Of course, based on your background, you are naturally stronger in some areas than others. However, you still have potential power untapped...use it wisely.")
          stat_adder(player, 10)
        elif background=="The Chosen One":
          passed=True
          player=TwoSouled(name)
          print("I see...welcome back, O reincarnation of the Chosen One.")
        else:
          background=input("Come on now! Don't tell me you came from nowhere! Are you a warrior, archer or mage?" + "\n") 
      print("\n"+"Each class has their own special abilities, and you must choose one to master right now."+"\n")
      ability_selector(player)
      print("And finally...what 3 items will you take with you when you first embark?")
      itemList=[Item("Great Potion", "Heals the user for a moderate amount.", 50), Item("Great Ether", "Restores a moderate amount of the user's MP.", 50), Item("Berserker Ale", "Doubles attack, but halves both defense stats.", 100), Item("Sage Scroll", "Increases magic attack and magic defense by 50%.", 100), Item("Cloak of Deception", "Doubles speed, but halves both attack stats.", 100)]
      itemNames=[]
      for item in itemList:
        itemNames.append(item.name.lower())
      while len(player.inventory)<3:
        for item in itemList:
          print(item.name)
          print(item.desc)
        choice=input()
        if choice.lower() not in itemNames: 
          print("No item of that name! \n")
        else:
          player.inventory.append(itemList[itemNames.index(choice.lower())])
          player.itemNames.append(itemList[itemNames.index(choice.lower())].name.lower())
          print("You took 1 " + choice + ". \n")
      print("It is time for you to head out on your journey. Best of luck, and may you have safe travels...")
      locationList=[]
      Tarrey=Town("Tarrey Town", 
      [Weapon("Steel Sword", "blade", "Physical", pdmg=10, cost=25), Weapon("Steel Bow", "bow", "Physical", pdmg=8, cost=20), Weapon("Journeyman's Rod", "rod", "Magical", mdmg=10, cost=40), Armor("Iron Chestplate", "heavy armor", pdef=8, mdef=3, spd=-3, cost=30), Armor("Reinforced Vest","light armor", pdef=6, mdef=2, cost=25), Armor("Journeyman's Robe", "robe", pdef=3, mdef=9, cost=35)], [Item("Potion", "Heals the user for a small amount.", cost=5), Item("Ether", "Restores a small amount of the user's MP.", cost=10)]) 
      Gans=Location("Gansfield Plains")
      locationList.append(Tarrey)
      locationList.append(Gans)
      locationList[1].story=Gansstory
      locationList[0].connect(locationList[1])
      player.location=locationList[0]
      player.recentTown=player.location
      overworld(player)
    elif choice.lower()=="close":
      return
    else:
      print("Invalid input."+"\n")
    
main()

