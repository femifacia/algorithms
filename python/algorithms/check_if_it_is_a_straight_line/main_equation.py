#!/usr/bin/env python3

class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        #at first I tryed to calculate a and b of the formula y = ax + b
        #if coordinates where for a line all y would have verfied this equation
        #but I get divsion by 0 cause a = y0 - y / x0 - x
        #So instead of doing a division a tryed another way.
        #if 3 points (x, y), (x0, y0), (x1,y1) are on the same right so they share the same "a"
        #so I can pose a1 == a2 =>
        # y0 - y / x0 - x = y0 - y1 / x0 - x1
        # So by doing product of the extremes is equal to the product of the means I have this
        # (y0 - y) * (x0 - x1) ==  (y0 - y1) * (x0 - x)
        # if equality test fail for a point a return False
         
        y_product = (coordinates[0][1] - coordinates[1][1])
        x_product = (coordinates[0][0] - coordinates[1][0])
        x0 = coordinates[0][0]
        y0 = coordinates[0][1]
        for x, y in coordinates[2:]:
            new_y_product = (y0 - y)
            new_x_product = (x0 - x)
            if (y_product * new_x_product != x_product * new_y_product):
                return False
        return True