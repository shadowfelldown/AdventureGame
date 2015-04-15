__author__ = 'Daniel'
import random
def wrap_list(lst, items_per_line=10):
    lines = []
    for i in range(0, len(lst), items_per_line):
        chunk = lst[i:i + items_per_line]
        line = ", ".join("{!r}".format(x) for x in chunk)
        lines.append(line)
    return "[" + ",\n ".join(lines) + "]"
mapSize = 100
mapList = [random.randrange(0,5,1) for _ in range (mapSize)]
print (wrap_list(mapList))

