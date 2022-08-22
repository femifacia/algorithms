#!/usr/bin/env python3

from os import remove
from collections import  deque

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.used = deque()
        self.dict = {}
        self.count = 0

    def get(self, key: int) -> int:
        if key in self.dict:
            if (key in self.used):
                self.used.remove(key)
            self.used.append(key)
            return (self.dict[key])
        else:
            return (-1)

    def put(self, key: int, value: int) -> None:
        #print(self.used)
        if (key in self.dict):
            if (key in self.used):
                self.used.remove(key)
            self.dict[key] = value
            self.used.append(key)
        elif (self.count < self.size):
            self.used.append(key)
            self.dict[key] = value
            self.count +=1
        else:
            evict = self.used.popleft()
            del self.dict[evict]
            if (evict in self.used):
                self.used.remove(evict)
            self.dict[key] = value
            self.used.append(key)
#            print("put",self.dict, "key",key, value, 'val')
#                print("hum", self.index)
                #del self.dict[self.index_dic[self.index]]
#                del self.index_dic[self.index]
#            print("putend",self.dict, "key",key, value, 'val')



# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(2,1)
obj.put(1,1)
obj.put(2,3)
obj.put(4,1)
print(obj.get(1))
print(obj.get(2))
obj.put(1,1)
obj.put(4,1)
print(obj.get(2))

# param_1 = obj.get(key)
# obj.put(key,value)