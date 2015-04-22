__author__ = 'dlpogue'
import map
import Player
import roomDescriptions
mapList = map.generate()
userPos, endPos, mapList, dispList = map.userplace(mapList)
roomDescriptions.generate()
descList = roomDescriptions.roomgenerator(mapList)
print(mapList)
#map.display(mapList)
description, Choices = map.roomchoices(mapList, userPos)
print userPos
print descList[userPos-1]
print Choices
raw_input('Which Way do you go?')
player.movement(choices[2], mapList)
#Player.distanceto(userPos,endPos)