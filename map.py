__author__ = "Daniel"
import random
def generate():
    mapSize = 100
    return [random.randrange(0,5,1) for _ in range (mapSize)]
def display(lst, items_per_line=10):
    lines = []
    for i in range(0, len(lst), items_per_line):
        chunk = lst[i:i + items_per_line]
        line = ", ".join("{!r}".format(x) for x in chunk)
        lines.append(line)
    print("[" + ",\n ".join(lines) + "]")

def userplace(usrpos, maplist):
    displist = list(maplist)

    displist[usrpos] = 'X'
    maplist[usrpos] = 1
    if usrpos > 50:
        randomplacevar = random.randrange(40, 50, 1)
        randomendpos = random.randrange(0, (usrpos - randomplacevar), 1)
    else:
        randomplacevar = random.randrange(40, 50, 1)
        randomendpos = random.randrange(49, (usrpos + randomplacevar), 1)

    displist[randomendpos] = 'W'
    maplist[randomendpos] = 5

    return usrpos, randomendpos, maplist, displist

def redraw(usrpos,endpos,maplist):
    displist = list(maplist)
    displist[usrpos] = 'X'
    displist[endpos] = 'W'
    return displist

def roomchoices(maplist,usrplace):
    choices = []
    rooms = [1, 2, 3]
    print (usrplace)
    try:
        if maplist[usrplace-10] in rooms:
            choices.append('NORTH')
        if maplist[usrplace+10] in rooms:
            choices.append('SOUTH')
        if usrplace % 10 != 9:
            if maplist[usrplace+1] in rooms:
                choices.append('EAST')
        if usrplace % 10 != 0:
            if maplist[usrplace-1] in rooms:
                choices.append('WEST')
    except IndexError:
            maplist[usrplace] = 'null'
    describe = 'There is a doorway to the', ', '.join(choices[0:-1]), 'and', choices[-1]
    return describe, choices
