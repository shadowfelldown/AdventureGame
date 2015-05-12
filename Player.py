import random
import map
__author__ = 'Daniel'
def options(choices):
    while True:
        try:
            userchoice = str(raw_input('What do you do?     '))
            if 'stuck' in userchoice.lower():
                return 'STUCK'
            if 'hint' in userchoice.lower():
                return 'HINT'
            if 'help' in userchoice.lower():
                return 'HELP'
            if 'quit' in userchoice.lower():
                sure = raw_input("are you sure? Y/N")
                if sure.lower() == 'y':
                    return 'QUIT'
                else:
                    continue
            if 'take' in userchoice.lower():
                if 'treasure' in userchoice.lower():
                    return 'TREASURE'
            if 'use' in userchoice.lower():
                if 'map' in userchoice.lower():
                    return 'MAP'
            if 'go' or 'proceed' in userchoice.lower():
                if any(ext in userchoice.upper() for ext in choices):
                    if 'north' in userchoice.lower():
                        return 'NORTH'
                    if 'south' in userchoice.lower():
                        return 'SOUTH'
                    if 'east' in userchoice.lower():
                        return 'EAST'
                    if 'west' in userchoice.lower():
                        return 'WEST'
                else:
                    print 'You cannot go that way'
                    continue
        except ValueError:
            print "Please enter a string"
        #better try again... Return to the start of the loop
            continue
        else:
            print "invalid entry, please type 'HELP' if you are stuck"
            continue



def distanceto(userpos,target,):
    if userpos > target:
        distance = round((userpos - target) / 10)
    else:
        distance = round((target - userpos) / 10)
    print "You are", distance, " rooms away from your goal"
    #once target function is defined, will be room name, i.e goal, treasure, exit.

def movement(direction,userpos,maplist,choices):
    if direction == 'NORTH':
        userpos = userpos-10
        print 'you proceed NORTH'
        return userpos
    if direction == 'SOUTH':
        userpos = userpos+10
        print 'you proceed SOUTH'
        return userpos
    if direction == 'EAST':
        userpos = userpos+1
        print 'you proceed EAST'
        return userpos
    if direction == 'WEST':
        userpos = userpos-1
        print 'you proceed WEST'
        return userpos
    else:
        print 'you cannot go that way'

        return userpos
