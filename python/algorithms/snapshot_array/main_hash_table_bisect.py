#!/usr/bin/env python3

#Perfect

from bisect import bisect_right

class SnapshotArray:

    def __init__(self, length: int):
        self.old = [None] * length
        self.new = [0] * length
        self.snap_array = [{} for _ in range(length)]
        self.snap_int = 0
        self.range = range(length)
        self.changed = set(self.range)
        

    def set(self, index: int, val: int) -> None:
        self.new[index] = val
        if self.new[index] == self.old[index] and index in self.changed:
            self.changed.remove(index)
        if self.new[index] != self.old[index] and not index in self.changed:
            self.changed.add(index)

    def snap(self) -> int:
        for i in self.changed:
            if self.new[i] != self.old[i]:
                self.old[i] = self.new[i]
                self.snap_array[i][self.snap_int] = self.new[i]
        self.snap_int += 1
        self.changed = set()
        return self.snap_int - 1
        

    def get(self, index: int, snap_id: int) -> int:
        index_arr = list(self.snap_array[index].keys())
        pos = bisect_right(index_arr, snap_id)
#        print(self.snap_array[index])
#        print(index_arr,index)
        return self.snap_array[index][index_arr[pos - 1]]
        


# Your SnapshotArray object will be instantiated and called as such:
obj = SnapshotArray(1)
print("snap", obj.snap())
print("snap", obj.snap())
obj.set(0,4)
print("snap", obj.snap())
print("get", obj.get(0,1))
obj.set(0,12)
print("get", obj.get(0,1))
print("snap", obj.snap())
print("get", obj.get(0,3))
