__author__ = 'dlpogue'
import os
import map
import Player
import roomDescriptions
import random
import sys
Map = 0
mapList = map.generate()
usrRandPos = random.randrange(0, 99, 1)
userPos, endPos, mapList, dispList = map.userplace(usrRandPos, mapList)
roomDescriptions.generate()
descList = roomDescriptions.roomgenerator(mapList)
#print(descList)
map.display(dispList)
while True:
    print chr(27) + "[2J"
    os.system('cls' if os.name == 'nt' else 'clear')
    if Map == 1:
        map.display(dispList)
        Map = 0
    description, Choices = map.roomchoices(mapList, userPos)
    #print userPos
    #print descList[userPos-1]
    print descList[userPos]
    print " ".join(description)
    #print userPos
    usrChoice = Player.options(Choices)
    #print usrChoice
    if usrChoice == 'QUIT':
        sys.exit(0)
    if usrChoice == 'HELP':
        map.help()
        continue
    if usrChoice == 'HINT':
        Player.distanceto(userPos, endPos)
        continue
    if usrChoice == 'STUCK':
        userPos = random.randrange(0, 99, 1)
        continue
    if usrChoice == 'MAP':
        Map = 1
        continue
    if usrChoice == 'TREASURE' and userPos == endPos:
        print "You reach out and open the TREASURE chest. Inside you find an incredible fortune in gemstones as well as a rune encrusted SWORD. \n"
        raw_input('press any key to take the SWORD...')
        print "As soon as your fingers touch the hilt of the beautiful sword, the dungeon around you begins to rumble \n \n 'YOU DARE TO STEAL MY TREASURE, HUMAN?' \n \n the booming voice seems to be coming from above you. \n"
        raw_input('press any key to look up...\n')
        print "You look upwards to find the source of the voice and find yourself staring into the largest Ruby that you have ever seen. It seems to be set into the rock above. \n You cannot see an obvious source of the voice, but you feel as if you are being watched. \n"
        raw_input('press any key to continue...\n')
        print "As you are watching the Ruby, the rock around it shifts and you realize that you are staring directly into the Ruby eye of a giant stone dragon. \n\n ' NOW YOU WILL DIE' \n \n"
        raw_input("to be continued...")
        break
    else:
        userPos = Player.movement(usrChoice, userPos, mapList, Choices)
#       print userPos
        dispList = map.redraw(userPos,endPos,mapList)
#       map.display(dispList)
        #Player.distanceto(userPos,endPos)
