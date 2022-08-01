#!/usr/bin/env python3

def closest_value(arr):
    arr.sort()
    val_min, index_min = min((arr[i] - arr[i - 1], i) for i in range(1, len(arr)))
    return (arr[index_min - 1], arr[index_min], val_min)

arr = [9, 4, -50, 0, 5, 2, 3, 78, 7, -10]
print(closest_value(arr))