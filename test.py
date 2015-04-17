__author__ = 'dlpogue'
import map
mapList = map.generate()
userPos, endPos, mapList = map.userplace(mapList)
print(mapList)
map.display(mapList)
map.roomchoices(mapList, userPos)