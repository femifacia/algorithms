#!/usr/bin/env python3

maxx = 1000

def func(i):
    if i == maxx:
        return
    print(i)
    func(i + 1)

func(0)