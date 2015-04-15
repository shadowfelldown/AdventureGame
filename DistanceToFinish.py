from UserPlace import userRandomPos, randomEndPos


__author__ = 'John'

if userRandomPos > randomEndPos:
    finishDistance = round((userRandomPos - randomEndPos) / 10)
else:
    finishDistance = round((randomEndPos - userRandomPos) / 10)

print()
print ("You are",finishDistance, "rooms away from the treasure!")




