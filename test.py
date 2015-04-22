__author__ = 'dlpogue'
import map
import Player
import roomDescriptions
mapList = map.generate()
userPos, endPos, mapList = map.userplace(mapList)
roomDescriptions.generate()
roomDescriptions.roomgenerator(mapList)
#print(mapList)
#map.display(mapList)
description, Choices = map.roomchoices(mapList, userPos)
print description[userPos]
print Choices
rawinput('Which Way do you go?')
player.movement(choices[2], mapList)
#Player.distanceto(userPos,endPos)