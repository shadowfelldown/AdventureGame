__author__ = 'John'
import random

room1 = "You enter a dusty room with a smooth cobblestone floor. \n\
It appears as though nobody has set food in here for years. \n"
room2 = 'The room is dark and you hear the faint trickle of water. \n\
There is a faint smell of earth and you see moss in the cracks in the floor.\n'
room3 = 'The floor in front of you crumbles away. \n\
It leaves behind a small path around the edge of the room,\n\
an impossibly deep chasm occupies the rest. \n'
room4 = 'Brightly lit torches cover the walls. \n\
What appears to be an altar rests in the center of the room. \n'
room5 = 'You are surrounded by mechanical noise and the clinking of gears.\n\
It appears as though you are in the heart of some sort of mechanism. \n'
room6 = 'You enter a small room, no more than two yards across, \n\
it appears as though there is some writing on the wall, but it is too dark to make out.\n'
room7 = 'Before you even set foot in the room, you could hear what was inside. \n\
Hundreds of animals line the walls in cages of varying size. The stench is unbearable. \n'
room8 = 'You feel like you have been here before, but you are unsure.'
room9 = "There is a small dried up fountain in the center of the room, \n\
it looks like it has'nt seen water in years. \n"
room10 = "An old man sits in a chair in the center of the room. \n\
Before you get a chance to speak he laughs maniacally and fanishes into thin air. \n"
room11 = 'You see sunlight as you enter the room, but to your dismay, \n\
it is coming from a skylight twenty feet above your head. \n'
room12 = 'You hear a constant rumbling. It would probably be a good idea to \n\
get out as soon as possible. \n'

rooms = [room1, room2, room3, room4, room5, room6, room7, room8, room9, room10, room11, room12]

print(rooms[random.randrange(0, 11, 1)])




