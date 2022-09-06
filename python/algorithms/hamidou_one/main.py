#!/usr/bin/env python3

import sys

fd = open(sys.argv[1], "r")
lines = fd.read().split("\n")
x_max, y_max = map(int, lines[0].split(" "))
instruction = len(lines)
orientation = "NESW"
orientation_add = [(0,1),(1, 0), (0, - 1), (-1, 0)]
i = 1

while (i < instruction):
    line_raw = lines[i].split(" ")
    x_t = int(line_raw[0])
    y_t = int(line_raw[1])
    o_t = line_raw[2]
    index_orientation = orientation.find(o_t)
    for j in lines[i + 1]:
        if (j == "G"):
            index_orientation = index_orientation - 1 if index_orientation > 0 else (len(orientation) - 1)
        elif (j == "D"):
            index_orientation = index_orientation + 1 if index_orientation < len(orientation) - 1 else 0
        else:
            x_add = orientation_add[index_orientation][0]
            y_add = orientation_add[index_orientation][1]
            if ((x_t == 0 and x_add < 0) or (x_t == x_max and x_add > 0)):
                continue
            if ((y_t == 0 and y_add < 0) or (y_t == y_max and y_add > 0)):
                continue
            x_t += x_add
            y_t += y_add
    o_t = orientation[index_orientation]
    print(x_t, y_t, o_t)
    i += 2
fd.close()