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
def movement(userpos,mapList,choices):
    direction = raw_input('Which Way do you go?\n')
    if direction == 'NORTH' and choices[0] == 'NORTH':
        userpos = userpos-10
        print 'you proceed NORTH'
    if direction == 'SOUTH' and choices[1] == 'SOUTH':
        userpos = userpos+10
        print 'you proceed SOUTH'
    if direction == 'EAST' and choices[2] == 'EAST':
        userpos = userpos+1
        print 'you proceed EAST'
    if direction == 'WEST' and choices[3] == 'WEST':
        userpos = userpos-1
        print 'you proceed WEST'
    else:
        print 'you cannot go that way'


