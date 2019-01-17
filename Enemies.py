import time
class Enemy():

  def __init__(self, name, atkType=None, hp=0, patk=0, pdef=0, matk=0, mdef=0, spd=0):
    self.name=name
    self.atkType=atkType
    self.maxhp=hp
    self.patk=patk
    self.pdef=pdef
    self.matk=matk
    self.mdef=mdef
    self.spd=spd
    self.currenthp=self.maxhp
    self.currentatk=self.patk
    self.currentdef=self.pdef
    self.currentmatk=self.matk
    self.currentmdef=self.mdef
    self.currentspd=self.spd

  def __gt__(self, other):
    return self.currentspd > other.currentspd
  
  def __st__(self, other):
    return self.currentspd < other.currentspd 

  def attack(self, target):
    print(self.name + " attacks!")
    time.sleep(1)
    if self.atkType=="Physical":
      damage=self.currentatk-target.currentdef
    elif self.atkType=="Magical":
      damage=self.currentmatk-target.currentmdef
    if damage<=0:
      damage=0
    target.currenthp-=damage
    print("Dealt " + str(damage) + " damage!")