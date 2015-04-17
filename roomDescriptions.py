__author__ = 'John'
import random
def generate():
    global rooms1
    rooms1 = []
    rooms1.append("You enter a dusty room with a smooth cobblestone floor. \n\
    It appears as though nobody has set food in here for years. \n")
    rooms1.append('The room is dark and you hear the faint trickle of water. \n\
    There is a faint smell of earth and you see moss in the cracks in the floor.\n')
    rooms1.append('The floor in front of you crumbles away. \n\
    It leaves behind a small path around the edge of the room,\n\
    an impossibly deep chasm occupies the rest. \n')
    rooms1.append('Brightly lit torches cover the walls of this chamber. \n\
    What appears to be an altar rests in the center of the room. \n')
    rooms1.append('You are surrounded by mechanical noise and the clinking of gears.\n\
    It appears as though you are in the heart of some sort of mechanism. \n')
    rooms1.append('You enter a small room, no more than two yards across, \n\
    it appears as though there is some writing on the wall, but it is too dark to make out.\n')
    rooms1.append('Before you even set foot in the room, you could hear what was inside. \n\
    Hundreds of animals line the walls in cages of varying size. The stench is unbearable. \n')
    rooms1.append('You feel like you have been here before, but you are unsure.')
    rooms1.append("There is a small dried up fountain in the center of the room, \n\
    it looks like it hasn't seen water in years. \n")
    rooms1.append("An old man sits in a chair in the center of the room. \n\
    Before you get a chance to speak he laughs maniacally and vanishes into thin air. \n")
    rooms1.append('You see sunlight as you enter the room, but to your dismay, \n\
    it is coming from a skylight twenty feet above your head. \n')
    rooms1.append('You hear a constant rumbling. It would probably be a good idea to \n\
    get out as soon as possible. \n')
    rooms1.append('This room contains nothing but a table small round fishbowl with a single goldfish swimming in it. \n\
    The goldfish winks at you. \n')
    rooms1.append('')
    return rooms1

def roomgenerator(maplist):
    disclist = maplist
    for x in maplist:
        if maplist[x] == 0 or 4:
            disclist[x] = 'There is a wall'
        if maplist[x] == 1:
            disclist[x] = rooms1.pop([random.randrange(0, len(rooms1), 1)])
#        if maplist[x] == 2:
#            #disclist[x] = rooms2.pop([random.randrange(0, len(rooms2), 1)])
#        if maplist[x] == 3:
#            disclist[x] = rooms3.pop([random.randrange(0, len(rooms3), 1)])
#        if maplist[x] == 4:
#            disclist[x] = rooms4.pop([random.randrange(0, len(rooms4), 1)])
    print (disclist)


