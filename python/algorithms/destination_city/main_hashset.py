#!/usr/bin/env python

from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cities_with_neighbors = set()
        all_cities = set()

        for i in paths:
            cities_with_neighbors.add(i[0])
#            print(all_cities)
            all_cities.add(i[0])
            all_cities.add(i[1])
        return (cities_with_neighbors ^ all_cities).pop()