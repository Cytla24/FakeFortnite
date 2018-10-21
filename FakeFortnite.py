#Fortnite
from random import randint

def Databank(x,y):
  if x == y and x != 0:
    a =input("Would You like to pick up the apple on the floor?Type Y/N \n")
    if a == "Y":
      User.action_pick("apple")
      a =input("Would You like to store the apple on the floor or plant it?Type S/P \n")
      if a == "E":
        pass
      elif a == "P":
        s = randint(0,3)
        if s == 0:
          print("Youve planted and gotten two times what you planted")
          User.action_plant("apple")
        else :
          print("Youve planted lost what you planted")
          User.action_remove("apple")
    else:
      return
  elif abs(x) == randint(0,3) and abs(y) == randint(0,3):
      a =input("Would You like to pick up the orange on the floor?Type Y/N \n")
      if a == "Y":
        User.action_pick("orange")
        a =input("Would You like to store the orange on the floor or plant it?Type E/P \n")
        if a == "S":
          pass
        elif a == "P":
          s = randint(0,1)
          if s == 0:
            print("Youve planted and gotten two times what you planted")
            User.action_plant("orange")
          else :
            print("Youve planted lost what you planted")
            User.action_remove("orange")
      else:
        return
  elif abs(x) == randint(3,6) and abs(y) == randint(0,3):
    a =input("Would You like to pick up the hotdog on the floor?Type Y/N \n")
    if a == "Y":
      User.action_pick("hotdog")
      a =input("Would You like to store the hotdog on the floor or plant it?Type E/P \n")
      if a == "S":
        pass
      elif a == "P":
        print("Who tries to plant a hotdog?")
        User.action_remove("hotdog")
    else:
      return    
  elif abs(x) == randint(0,3) and abs(y) == randint(3,6):
    a =input("Would You like to pick up the pineapple on the floor?Type Y/N \n")
    if a == "Y":
      User.action_pick("pineapple")
      a =input("Would You like to store the pineapple on the floor or plant it?Type E/P \n")
      if a == "S":
        pass
      elif a == "P":
        s = randint(0,1)
        if s == 0:
          print("Youve planted and gotten two times what you planted")
          User.action_plant("pineapple")
        else :
          print("Youve planted lost what you planted")
          User.action_remove("pineapple")    
    else:
      return
  elif abs(x) == randint(3,6) and abs(y) == randint(3,6):
    a =input("Would You like to pick up the wood on the floor?Type Y/N \n")
    if a == "Y":
      User.action_pick("wood")
      a =input("Would You like to eat the wood on the floor or plant it?Type E/P \n")
      if a == "E":
        User.action_eat("wood")
      elif a == "P":
        User.action_plant("wood")
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
  def action_eat(self,item_a):
    self.inventory.remove(item_a)
  def action_eata(self):
    self.inventory.pop()
  def action_remove(self,item_a):
    self.inventory.remove(item_a)
  def action_plant(self,item_a):
    self.inventory.append(item_a)
  def action_inventory(self):
    return self.inventory

User = Position(0,0)
print("WELCOME GREAT GRASSHOPPER")
print("Clue: If you perform actions 5 times in a row without eating you die. If you have food and wish to eat type in eat. see how long you can last\n\n ")
action_x = input("what is you course of action(up,down,right,left,eat,pick,inventory,quit)\n")

int_i = 0
while action_x != "quit" and int_i<5:
  
  
  if action_x == "up":
    User.action_up()
  elif action_x == "down":
    User.action_down()
  elif action_x == "left":
    User.action_left()
  elif action_x == "right":
    User.action_right()
  elif action_x == "pick":
    User.action_pick()
  elif action_x == "eat":
    if User.action_inventory() != []:
      int_i = 0
      User.action_eata()
    else:
      int_i = 1000000
      print("YOU DEADDDD HAHA, enjoy your last move warrior as I sip your Bones")
  elif action_x == "inventory":
    b= ""
    for i in User.action_inventory():
      b += i
    print(b)
  else:
    print("invalid action")
  
  int_i+=1
  action_x = input("what is your next course of action\n")



print("GoodBye Great Warrior!")
