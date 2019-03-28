# FakeFortnite

a basic text game. allows a user to walk in different directions and pick up objects. To be more specific, it supports the following commands:
|up-
move user up one space|
down - 
move user down one space|
left -
more user left one space|
right - 
move user right one space|
pick up -
add whatever object the user is standing on to their inventory|
inventory -
list the objects that the user has in their inventory|
quit -
ends the game|

After each turn,it prints the location that the user is at. it uses XY coordinates to track the user's location and have the user start at (0, 0). If the user is ever standing on an object, it prints the name of the object. Objects are located at specific coordinates, or they can appear randomly.

This code provided a great opportunity to flex my creative ambition.


Sample program output:
>>> Welcome to Fortnite Classic!
>>> You're standing at 0,0
>>> What is your command?
 up
>>> You're standing at 0,1
>>> What is your command?
 left
>>> You're standing at -1,1
>>> What is your command?
 left
>>> You're standing at -2,1
>>> You're standing on the object: pizza
>>> What is your command?
 pick up
>>> You're standing at -2,1
>>> What is your command?
 down
>>> You're standing at -2,0
>>> You're standing on the object: shoe
>>> What is your command?
 pick up
>>> You're standing at -2,0
>>> What is your command?
 inventory
>>> You're inventory is: pizza, shoe
