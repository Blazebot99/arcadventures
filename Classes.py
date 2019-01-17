from Functions import battle_loop
from Enemies import Enemy
import time

class Player():
  
  def __init__(self, name):
    self.name=name
    self.inventory=[]
    self.itemNames=[]
    self.equipment=[]
    self.equipmentNames=[]
    self.accessory=None
    self.exp=None
    self.level=None
    self.gold=100
    self.location=None
    self.recentTown=None
    self.poison=None
    self.stun=None
    self.moved=False

  def __gt__(self, other):
    return self.currentspd > other.currentspd
  
  def __st__(self, other):
    return self.currentspd < other.currentspd 

  def equipArmor(self, armor):
    if armor.arT not in self.usableArmor:
      print("Can't use this armor!")
    elif self.armor is None:
      self.armor=armor
      self.currentatk+=self.armor.pdmg
      self.currentdef+=self.armor.pdef
      self.currentmatk+=self.armor.mdmg
      self.currentmdef+=self.armor.mdef
      self.currentspd+=self.armor.spd
      self.equipment.remove(armor)
      self.equipmentNames.remove(armor.name.lower())
    else:
      self.currentatk-=self.armor.pdmg
      self.currentdef-=self.armor.pdef
      self.currentmatk-=self.armor.mdmg
      self.currentmdef-=self.armor.mdef
      self.currentspd-=self.armor.spd
      self.equipment.append(self.armor)
      self.equipmentNames.append(self.armor.name.lower())
      self.armor=armor
      self.currentatk+=self.armor.pdmg
      self.currentdef+=self.armor.pdef
      self.currentmatk+=self.armor.mdmg
      self.currentmdef+=self.armor.mdef
      self.currentspd+=self.armor.spd
      self.equipment.remove(armor)
      self.equipmentNames.remove(armor.name.lower())

  def equipWeapon(self, weapon):
    if weapon.wT not in self.usableWeapons:
      print("Can't use that weapon!")
    elif self.weapon is None:
      self.weapon=weapon
      self.currentatk+=self.weapon.pdmg
      self.currentdef+=self.weapon.pdef
      self.currentmatk+=self.weapon.mdmg
      self.currentmdef+=self.weapon.mdef
      self.currentspd+=self.weapon.spd
      self.equipment.remove(weapon)
      self.equipmentNames.remove(weapon.name.lower())
    else:
      self.currentatk-=self.weapon.pdmg
      self.currentdef-=self.weapon.pdef
      self.currentmatk-=self.weapon.mdmg
      self.currentmdef-=self.weapon.mdef
      self.currentspd-=self.weapon.spd
      self.equipment.append(self.weapon)
      self.equipmentNames.append(self.weapon.name.lower())
      self.weapon=weapon
      self.currentatk+=self.weapon.pdmg
      self.currentdef+=self.weapon.pdef
      self.currentmatk+=self.weapon.mdmg
      self.currentmdef+=self.weapon.mdef
      self.currentspd+=self.weapon.spd
      self.equipment.remove(weapon)
      self.equipmentNames.remove(weapon.name.lower())
  
  def equipAccessory(self, accessory):
    pass

  def attack(self, target):
    print(self.name + " attacks with " + self.weapon.name + "!")
    time.sleep(1)
    if self.weapon.aT=="Physical":
      damage=self.currentatk-target.currentdef
      target.currenthp-=damage
    elif self.weapon.aT=="Magical":
      damage=self.currentmatk-target.currentmdef
      target.currenthp-=damage
    if damage<=0:
      damage=0
    print("Dealt "+ str(damage) + " damage to " + target.name +"!")
  
  def use_item(self, item):
    if item.unique==True:
      print("There's a time and place for everything...but that item can't be used right now.")
    if "Heals the user for a small amount" in item.desc:
      if self.currenthp==self.maxhp:
        print("Your HP is full!")
      elif self.currenthp+20>self.maxhp:
        self.currenthp=self.maxhp
        print("Used " + item.name + ". Restored " + str(self.maxhp-self.currenthp) + " HP.")
        self.inventory.remove(item)
        self.itemNames.remove(item.name.lower())
      else:
        self.currenthp+=20
        print("Used " + item.name + ". Restored 20 HP.")
        self.inventory.remove(item)
        self.itemNames.remove(item.name.lower())
    if "Restores a small amount of the user's MP" in item.desc:
      if self.currentmp==self.maxmp:
        print("Your MP is full!")
      elif self.currentmp+15>self.maxmp:
        self.currentmp=self.maxmp
        print("Used " + item.name + ". Restored " + str(self.maxmp-self.currentmp) + " MP.")
        self.inventory.remove(item)
        self.itemNames.remove(item.name.lower())
      else:
        self.currentmp+=15
        print("Used " + item.name + ". Restored 15 MP.")
        self.inventory.remove(item)
        self.itemNames.remove(item.name.lower())    
    if "Heals the user for a moderate amount" in item.desc:
      if self.currenthp==self.maxhp:
        print("Your HP is full!")
      elif self.currenthp+50>self.maxhp:
        self.currenthp=self.maxhp
        print("Used " + item.name + ". Restored " + str(self.maxhp-self.currenthp) + " HP.")
        self.inventory.remove(item)
        self.itemNames.remove(item.name.lower())
      else:
        self.currenthp+=50
        print("Used " + item.name + ". Restored 50 HP.")
        self.inventory.remove(item)
        self.itemNames.remove(item.name.lower())
    if "Restores a moderate amount of the user's MP" in item.desc:
      if self.currentmp==self.maxmp:
        print("Your MP is full!")
      elif self.currentmp+35>self.maxmp:
        self.currentmp=self.maxmp
        print("Used " + item.name + ". Restored " + str(self.maxmp-self.currentmp) + " MP.")
        self.inventory.remove(item)
        self.itemNames.remove(item.name.lower())
      else:
        self.currentmp+=35
        print("Used " + item.name + ". Restored 35 MP.")
        self.inventory.remove(item)
        self.itemNames.remove(item.name.lower())
    if "attack" in item.desc or "defense" in item.desc or "speed" in item.desc or "magic attack" in item.desc or "magic defense" in item.desc:
      print("That item can only be used in battle!")
  
  def use_battle_item(self, item):
    if item.unique==True:
      print("There's a time and place for everything...but that item can't be used right now.")
    if "Heals the user for a small amount" in item.desc:
      if self.currenthp==self.maxhp:
        print("Your HP is full!")
      elif self.currenthp+20>self.maxhp:
        self.currenthp=self.maxhp
        print("Used " + item.name + ". Restored " + str(self.maxhp-self.currenthp) + " HP.")
        self.inventory.remove(item)
        self.itemNames.remove(item.name.lower())
      else:
        self.currenthp+=20
        print("Used " + item.name + ". Restored 20 HP.")
        self.inventory.remove(item)
        self.itemNames.remove(item.name.lower())
    if "Restores a small amount of the user's MP" in item.desc:
      if self.currentmp==self.maxmp:
        print("Your MP is full!")
      elif self.currentmp+15>self.maxmp:
        self.currentmp=self.maxmp
        print("Used " + item.name + ". Restored " + str(self.maxmp-self.currentmp) + " MP.")
        self.inventory.remove(item)
        self.itemNames.remove(item.name.lower())
      else:
        self.currentmp+=15
        print("Used " + item.name + ". Restored 15 MP.")
        self.inventory.remove(item)
        self.itemNames.remove(item.name.lower())    
    if "Heals the user for a moderate amount" in item.desc:
      if self.currenthp==self.maxhp:
        print("Your HP is full!")
      elif self.currenthp+50>self.maxhp:
        self.currenthp=self.maxhp
        print("Used " + item.name + ". Restored " + str(self.maxhp-self.currenthp) + " HP.")
        self.inventory.remove(item)
        self.itemNames.remove(item.name.lower())
      else:
        self.currenthp+=50
        print("Used " + item.name + ". Restored 50 HP.")
        self.inventory.remove(item)
        self.itemNames.remove(item.name.lower())
    if "Restores a moderate amount of the user's MP" in item.desc:
      if self.currentmp==self.maxmp:
        print("Your MP is full!")
      elif self.currentmp+35>self.maxmp:
        self.currentmp=self.maxmp
        print("Used " + item.name + ". Restored " + str(self.maxmp-self.currentmp) + " MP.")
        self.inventory.remove(item)
        self.itemNames.remove(item.name.lower())
      else:
        self.currentmp+=35
        print("Used " + item.name + ". Restored 35 MP.")
        self.inventory.remove(item)
        self.itemNames.remove(item.name.lower())
    if item.name=="Berserker Ale":
      self.currentatk*=2
      self.currentdef=int(self.currentdef*0.5)
      self.currentmdef=int(self.currentmdef*0.5)
      print("Used berserker ale. Attack doubled! Defense and magic defense halved!")
      self.inventory.remove(item)
      self.itemNames.remove(item.name.lower())
    if item.name=="Sage Scroll":
      self.currentmatk=int(self.currentmatk*1.5)
      self.currentmdef=int(self.currentmdef*1.5)
      print("Used sage scroll. Magic attack and magic defense buffed!")
      self.inventory.remove(item)
      self.itemNames.remove(item.name.lower())
    if item.name=="Cloak of Deception":
      self.currentspd*=2
      self.currentatk=int(self.currentatk*0.5)
      self.currentmatk=int(self.currentmatk*0.5)
      print("Used cloak of deception. Speed doubled! Attack and magic attack halved!")
      self.inventory.remove(item)
      self.itemNames.remove(item.name.lower())

class Warrior(Player):

  def __init__(self, name):
    Player.__init__(self, name)
    self.chosenOne=False
    self.weapon=Weapon("Iron Shortsword", "blade", "Physical", cost=10, pdmg=7)
    self.armor=Armor("Leather Cuirass", "light armor", cost=10, pdef=5)
    self.maxhp=35
    self.maxmp=13
    self.patk=25
    self.pdef=20
    self.matk=10
    self.mdef=10
    self.spd=15
    self.currenthp=self.maxhp
    self.currentmp=self.maxmp
    self.currentatk=self.patk+self.weapon.pdmg+self.armor.pdmg
    self.currentdef=self.pdef+self.weapon.pdef+self.armor.pdef
    self.currentmatk=self.matk+self.weapon.mdmg+self.armor.mdmg
    self.currentmdef=self.mdef+self.weapon.mdef+self.armor.mdef
    self.currentspd=self.spd+self.weapon.spd+self.armor.spd
    self.usableWeapons=["blade"]
    self.usableArmor=["medium armor", "heavy armor"]
    self.classAbilities=[Ability("Guard Break", 3, "A heavy blow that lowers an enemy's defense."), Ability("Whirlwind Strike", 7, "The user executes a spinning attack to damage all enemies."), Ability("Feint", 4, "Fake an attack to confuse the enemy, lowering their speed.")]
    self.chosenAbilities=[]

  def learn_ability(self, index):
    if self.classAbilities[index] in self.chosenAbilities:
      print("You already have that ability!" + "\n")
    else:
      self.chosenAbilities.append(self.classAbilities[index])
      print("You learned "+ self.classAbilities[index].name+"."+"\n")

class Archer(Player):

  def __init__(self, name):
    Player.__init__(self, name)
    self.chosenOne=False
    self.weapon=Weapon("Wooden Bow", "bow", "Physical", cost=10, pdmg=5)
    self.armor=Armor("Camo Vest", "light armor", cost=10, pdef=4, mdef=2)
    self.maxhp=30
    self.maxmp=20
    self.patk=20
    self.pdef=10
    self.matk=15
    self.mdef=10
    self.spd=25
    self.currenthp=self.maxhp
    self.currentmp=self.maxmp
    self.currentatk=self.patk+self.weapon.pdmg+self.armor.pdmg
    self.currentdef=self.pdef+self.weapon.pdef+self.armor.pdef
    self.currentmatk=self.matk+self.weapon.mdmg+self.armor.mdmg
    self.currentmdef=self.mdef+self.weapon.mdef+self.armor.mdef
    self.currentspd=self.spd+self.weapon.spd+self.armor.spd
    self.usableWeapons=["bow"]
    self.usableArmor=["light armor"]
    self.classAbilities=[Ability("Snipe", 4, "An attack that never misses and is more likely to be a critical hit."), Ability("Camouflage", 3, "Increases the user's speed."), Ability("Multishot", 7, "Shoots at one enemy twice.")]
    self.chosenAbilities=[]

  def learn_ability(self, index):
    if self.classAbilities[index] in self.chosenAbilities:
      print("You already have that ability!" + "\n")
    else:
      self.chosenAbilities.append(self.classAbilities[index])
      print("You learned "+ self.classAbilities[index].name+"."+"\n")

class Mage(Player):

  def __init__(self, name):
    Player.__init__(self, name)
    self.chosenOne=False
    self.weapon=Weapon("Acolyte's Rod", "rod", "Magical", cost=10, mdmg=7)
    self.armor=Armor("Acolyte's Robe", "robe", cost=10, pdef=1, mdef=5)
    self.maxhp=25
    self.maxmp=30
    self.patk=5
    self.pdef=5
    self.matk=25
    self.mdef=25
    self.spd=20
    self.currenthp=self.maxhp
    self.currentmp=self.maxmp
    self.currentatk=self.patk+self.weapon.pdmg+self.armor.pdmg
    self.currentdef=self.pdef+self.weapon.pdef+self.armor.pdef
    self.currentmatk=self.matk+self.weapon.mdmg+self.armor.mdmg
    self.currentmdef=self.mdef+self.weapon.mdef+self.armor.mdef
    self.currentspd=self.spd+self.weapon.spd+self.armor.spd
    self.usableWeapons=["rod"]
    self.usableArmor=["robe"]
    self.classAbilities=[Ability("Ring of Magic", 5, "A spell that increases the user's magical power."), Ability("Prism Shock", 3, "Hits the enemy's physical defense rather than magical defense."), Ability("Tri-Elemental", 10, "Uses fire, ice, and lightning to strike the target all at once.")]
    self.chosenAbilities=[]

  def learn_ability(self, index):
    if self.classAbilities[index] in self.chosenAbilities:
      print("You already have that ability!" + "\n")
    else:
      self.chosenAbilities.append(self.classAbilities[index])
      print("You learned "+ self.classAbilities[index].name+"."+"\n")

class TwoSouled(Player):

  def __init__(self, name):
    Player.__init__(self, name)
    self.chosenOne=True
    self.weapon=Weapon("Soul Calibur", "greatsword", "Magical", cost=0, pdmg=50, mdmg=250)
    self.secondWeapon=Weapon("Soul Edge", "greatsword", "Physical", cost=0, pdmg=250, mdmg=50)
    self.armor=Armor("Aliquaster", "chaoA", cost=0, pdef=200, mdef=200)
    self.maxhp=3000
    self.maxmp=2000
    self.patk=100
    self.pdef=100
    self.matk=150
    self.mdef=150
    self.spd=325
    self.currenthp=self.maxhp
    self.currentmp=self.maxmp
    self.currentatk=self.patk+self.weapon.pdmg+self.armor.pdmg + self.secondWeapon.pdmg
    self.currentdef=self.pdef+self.weapon.pdef+self.armor.pdef
    self.currentmatk=self.matk+self.weapon.mdmg+self.armor.mdmg+self.secondWeapon.mdmg
    self.currentmdef=self.mdef+self.weapon.mdef+self.armor.mdef
    self.currentspd=self.spd+self.weapon.spd+self.armor.spd
    self.usableWeapons=["greatsword", "chaoS"]
    self.usableArmor=["light armor", "medium armor", "heavy armor", "chaoA"]
    self.classAbilities=[]
    self.chosenAbilities=[]
    self.inventory.append(Item("Ilona's Eye", "The pendant of my dear departed sister...she must be avenged.", unique=True))
    self.itemNames.append("ilona's eye")

  def attack(self, target):
    print(self.name + " attacks with " + self.weapon.name +"!")
    if self.weapon.aT=="Physical":
      damage=self.currentatk-target.currentdef
    elif self.weapon.aT=="Magical":
      damage=self.currentmatk-target.currentmdef
    target.currenthp-=damage
    if damage<=0:
      damage=0
    time.sleep(1)
    print("Dealt "+ str(damage) + " damage to " + target.name +"!")
    time.sleep(1)
    print(self.name + " attacks with " + self.secondWeapon.name + "!")
    if self.secondWeapon.aT=="Physical":
      damage=self.currentatk-target.currentdef
    elif self.secondWeapon.aT=="Magical":
      damage=self.currentmatk-target.currentmdef
      target.currenthp-=damage
    if damage<=0:
      damage=0
    time.sleep(1)
    print("Dealt "+ str(damage) + " damage to " + target.name +"!")


class Ability():
  
  def __init__(self, name, mana, desc):
    self.name=name
    self.cost=mana
    self.desc=desc

  def description(self):
    print(self.desc)

class Equipment():

  def __init__(self, name, pdmg=0, mdmg=0, pdef=0, mdef=0, spd=0, effects=[], cost=0):
    self.name=name
    self.pdmg=pdmg
    self.mdmg=mdmg
    self.pdef=pdef
    self.mdef=mdef
    self.spd=spd
    self.effects=effects
    self.cost=cost

class Weapon(Equipment):

  def __init__(self, name, weaponType, attackType, pdmg=0, mdmg=0, pdef=0, mdef=0, spd=0, effects=[], cost=0):
    Equipment.__init__(self, name, pdmg, mdmg, pdef, mdef, spd, effects, cost)
    self.wT=weaponType
    self.aT=attackType

class Armor(Equipment):

  def __init__(self, name, armorType, pdmg=0, mdmg=0, pdef=0, mdef=0, spd=0, effects=[], cost=0):
    Equipment.__init__(self, name, pdmg, mdmg, pdef, mdef, spd, effects, cost)
    self.arT=armorType

class Item():
  
  def __init__(self, name, desc, unique=False, cost=0):
    self.name=name
    self.desc=desc
    self.cost=cost
    self.unique=unique

class Location():

  def __init__(self, name, storyline=None):
    self.name=name
    self.visited=False
    self.connections=[]
    self.connectionNames=[]
    self.story=storyline
    self.cleared=False
    
  def connect(self, other):
    self.connections.append(other)
    other.connections.append(self)
    self.connectionNames.append(other.name.lower())
    other.connectionNames.append(self.name.lower())
  
  def story_continue(self, player):
    index=0
    enemylist=[]
    name=None
    atkType=None
    hp=None
    patk=None
    pdef=None
    matk=None
    mdef=None
    spd=None
    for dialogue in self.story:
      if dialogue=="Initiate Battle":
        i=index 
        while True:
          i+=1
          dialogue=self.story[i]
          if dialogue=="end":
            break
          for x, term in enumerate(dialogue):
            if x==0:
              name=term
            elif x==1:
              atkType=term
            elif x==2:
              hp=term
            elif x==3:
              patk=term
            elif x==4:
              pdef=term
            elif x==5:
              matk=term
            elif x==6:
              mdef=term
            elif x==7:
              spd=term
          enemylist.append(Enemy(name, atkType, hp, patk, pdef, matk, mdef, spd))
        battle_loop(player, enemylist)
        if player.currenthp<=0:
          break
      elif type(dialogue)==type("") and dialogue!="end":
        print(dialogue)
        time.sleep(1)
      index+=1
    if player.currenthp>0:
      self.cleared=True
        
class Town(Location):

  def __init__(self, name, equipment, items, storyline=None):
    Location.__init__(self, name, storyline)
    self.items=items
    self.equipment=equipment
    self.itemNames=[]
    for item in items:
      self.itemNames.append(item.name.lower())
    self.equipmentNames=[]
    for equip in equipment:
      self.equipmentNames.append(equip.name.lower())