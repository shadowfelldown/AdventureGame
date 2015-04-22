__author__ = "Daniel"
def generate():
    import random
    mapSize = 100
    return [random.randrange(0,5,1) for _ in range (mapSize)]
def display(lst, items_per_line=10):
    lines = []
    for i in range(0, len(lst), items_per_line):
        chunk = lst[i:i + items_per_line]
        line = ", ".join("{!r}".format(x) for x in chunk)
        lines.append(line)
    print("[" + ",\n ".join(lines) + "]")


def userplace(maplist):
    userrandompos = random.randrange(0, 99, 1)

    maplist[userrandompos] = 'X'

    if userrandompos > 50:
        randomplacevar = random.randrange(40, 50, 1)
        randomendpos = random.randrange(0, (userrandompos - randomplacevar), 1)
    else:
        randomplacevar = random.randrange(40, 50, 1)
        randomendpos = random.randrange(49, (userrandompos + randomplacevar), 1)

    maplist[randomendpos] = 'W'

    return userrandompos, randomendpos, maplist

def roomchoices(maplist,usrplace):
    choices = []
    if maplist[usrplace-10] != 0:
        choices.append('NORTH')
    if maplist[usrplace+10] != 0:
        choices.append('SOUTH')
    if maplist[usrplace+1] != 0:
        choices.append('EAST')
    if maplist[usrplace-1] != 0:
        choices.append('WEST')
    describe = 'There is a doorway to the', ', '.join(choices[0:-1]), 'and', choices[-1]
    return describe, choices
