from WrapList import mapList
import random
__author__ = 'John'

userRandomPos = random.randrange(0,99,1)

mapList.insert(userRandomPos, "x")



if userRandomPos > 50:
    randomPlaceVar = random.randrange(40,50,1)
    randomEndPos = random.randrange(0,(userRandomPos - randomPlaceVar),1 )
else:
    randomPlaceVar = random.randrange(40,50,1)
    randomEndPos = random.randrange(49,(userRandomPos + randomPlaceVar),1 )

mapList.insert(randomEndPos, "[]")


print (userRandomPos)
print(randomEndPos)
print (mapList)




