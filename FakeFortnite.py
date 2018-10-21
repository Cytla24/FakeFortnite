#Fortnite
from random import randint

def Databank(x,y):
  if x == y and x != 0:
    a =input("Would You like to pick up the pizza on the floor?Type Y/N \n")
    if a == "Y":
      User.action_pick("pizza")
    else:
      return
  elif abs(x) == randint(0,3) and abs(y) == randint(0,3):
      int_i = 0
      Int_j = 0
      a =input("Would You like to pick up the mustard on the floor?Type Y/N \n")
      if a == "Y":
        User.action_pick("mustard")
      else:
        return
  elif abs(x) == randint(3,6) and abs(y) == randint(0,3):
    a =input("Would You like to pick up the hotdog on the floor?Type Y/N \n")
    if a == "Y":
      User.action_pick("hotdog")
    else:
      return    
  elif abs(x) == randint(0,3) and abs(y) == randint(3,6):
    a =input("Would You like to pick up the burger on the floor?Type Y/N \n")
    if a == "Y":
      User.action_pick("burger")
    else:
      return
  elif abs(x) == randint(3,6) and abs(y) == randint(3,6):
    a =input("Would You like to pick up the wood on the floor?Type Y/N \n")
    if a == "Y":
      User.action_pick("wood")
    else:
      return         
class Position:
  def __init__(self,x,y):
    self.x = x
    self.y = y
    self.inventory = []

  def action_up(self):
    self.y += 1
    print("Your new position is (" , self.x,",",self.y , ")")
    Databank(self.x,self.y)
    return
  def action_down(self):
    self.y -= 1
    print("Your new position is (" , self.x,",",self.y , ")")
    Databank(self.x,self.y)
    return 
  def action_left(self):
    self.x -= 1
    print("Your new position is (" , self.x,",",self.y , ")")
    Databank(self.x,self.y)
    return 
  def action_right(self):
    self.x += 1
    print("Your new position is (" , self.x,",",self.y , ")")
    Databank(self.x,self.y)
    return 
  def action_pick(self, item_a):
    self.inventory.append(item_a)
    return self.inventory
  def action_inventory(self):
    return self.inventory

User = Position(0,0)
print("WELCOME GREAT GRASSHOPPER")
action_x = input("what is you course of action\n")


while action_x != "quit":
  
  
  if action_x == "up":
    User.action_up()
  elif action_x == "down":
    User.action_down()
  elif action_x == "left":
    User.action_left()
  elif action_x == "right":
    User.action_right()
  elif action_x == "pick up":
    User.action_pick()
  elif action_x == "inventory":
    b= " "
    for i in User.action_inventory():
      b += i
    print(b)
  else:
    print("invalid action")
  
  
  action_x = input("what is your course of action\n")



print("GoodBye Great Warrior!")
