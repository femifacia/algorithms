#!/usr/bin/env python3

class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.arr = [-1] * capacity
        self.dict = {}
        self.index = 0
        self.index_dic = {}
        self.count = 0

    def get(self, key: int) -> int:
        #print(self.dict)
        if key in self.dict:
            return (self.dict[key])
        else:
            return (-1)

    def put(self, key: int, value: int) -> None:
        if (self.count <= self.size - 1):
            self.dict[key] = value
            self.index_dic[self.index] = key
            self.index += 1 if (self.index + 1 <self.size ) else 0
            self.count +=1
        else:
            print("put",self.dict, "key",key, value, 'val')
#                print("hum", self.index)
            if (self.index_dic[self.index] in self.dict):
                del self.dict[self.index_dic[self.index]]
            self.dict[key] = value
#                del self.index_dic[self.index]
            self.index_dic[self.index] = key
            self.index = self.index - 1 if (self.index > 0) else self.size - 1
            print("putend",self.dict, "key",key, value, 'val')



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