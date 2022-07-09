#!/usr/bin/python3.8

import math

def get_max_bin(nbr):
    maxx = []
    for a in range(nbr):
        maxx.append(1)
    return (maxx)

def get_mini_bin(nbr):
    mini = []
    for a in range(nbr):
        mini.append(0)
    return (mini)

def plus(nbr, pos):
    if (nbr[pos] == 0):
        nbr[pos] = 1
    else:
        nbr[pos] = 0
        nbr = plus(nbr, pos + 1)
    return (nbr)

if __name__ == "__main__":
    array = []
    listew = []
    nbr = input("enter a number\n")
    nbr = int(nbr)
    size = get_max_bin(nbr)
    mini = get_mini_bin(nbr)
    print(mini, '\n')
    while (mini != size):
        mini = plus(mini, 0)
        mini.reverse()
        print(mini)
        listew.append(mini.copy())
        print(listew)
        mini.reverse()
    print(listew)
        #print("a")

    #print("the size is", nbr, "high number is\n", size, "\n")
