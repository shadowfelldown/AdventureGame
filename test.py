__author__ = 'dlpogue'
import map
import Player
import roomDescriptions
import random
mapList = map.generate()
usrRandPos = random.randrange(0, 99, 1)
userPos, endPos, mapList, dispList = map.userplace(usrRandPos, mapList)
roomDescriptions.generate()
descList = roomDescriptions.roomgenerator(mapList)
#print(descList)
map.display(dispList)
treasure = 0
while treasure != 1:
    description, Choices = map.roomchoices(mapList, userPos)
    #print userPos
    #print descList[userPos-1]
    print Choices
    print userPos
    userPos = Player.movement(userPos, mapList, Choices)
    print userPos
    dispList = map.redraw(userPos,endPos,mapList)
    map.display(dispList)
    #Player.distanceto(userPos,endPos)