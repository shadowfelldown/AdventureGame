import random
import map
__author__ = 'Daniel'
def distanceto(userpos,target,):
    if userpos > target:
        distance = round((userpos - target) / 10)
    else:
        distance = round((target - userpos) / 10)
    return print ("You are", distance, " rooms away from your goal")
    #once target function is defined, will be room name, i.e goal, treasure, exit.
def movement(userpos,mapList,direction)

