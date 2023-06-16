#!/usr/bin/env python3

#Memory exceed


class SnapshotArray:

    def __init__(self, length: int):
        self.array = [0] * length
        self.snap_array = []
        self.snap_int = 0
        

    def set(self, index: int, val: int) -> None:
        self.array[index] = val
        

    def snap(self) -> int:
        self.snap_array.append(self.array[:])
        self.snap_int += 1
        return self.snap_int - 1
        

    def get(self, index: int, snap_id: int) -> int:
        return self.snap_array[snap_id][index]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)