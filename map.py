__author__ = "Daniel"
def generate()
    import random
    mapSize = 100
    mapList = [random.randrange(0,5,1) for _ in range (mapSize)]
def display(lst, items_per_line=10):
    lines = []
    lst2 = lst
    for i in range(0, len(lst2), items_per_line):
        chunk = lst2[i:i + items_per_line]
        line = ", ".join("{!r}".format(x) for x in chunk)
        lines.append(line)
    return "[" + ",\n ".join(lines) + "]"
print (wrap_list(mapList))