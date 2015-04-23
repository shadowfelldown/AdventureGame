import random
import map
__author__ = 'Daniel'
def distanceto(userpos,target,):
    if userpos > target:
        distance = round((userpos - target) / 10)
    else:
        distance = round((target - userpos) / 10)
    print "You are", distance, " rooms away from your goal"
    #once target function is defined, will be room name, i.e goal, treasure, exit.
def movement(userpos,maplist,choices):
    direction = raw_input('Which Way do you go?\n')
    if direction == 'NORTH' and maplist[userpos-10] != 0:
        userpos = userpos-10
        print 'you proceed NORTH'
        return userpos
    if direction == 'SOUTH' and maplist[userpos+10] != 0:
        userpos = userpos+10
        print 'you proceed SOUTH'
        return userpos
    if direction == 'EAST' and maplist[userpos-1] != 0:
        userpos = userpos+1
        print 'you proceed EAST'
        return userpos
    if direction == 'WEST' and maplist[userpos+1] != 0:
        userpos = userpos-1
        print 'you proceed WEST'
        return userpos
    else:
        print 'you cannot go that way'

        return userpos
