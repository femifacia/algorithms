#!/usr/bin/env python3

from os import remove

class LRUCache:

    class NodeList:
        def __init__(self, key, val, prev=None, nextt=None) -> None:
            self.key = key
            self.val= val
            self.prev = prev
            self.next = nextt
            pass

    def __init__(self, capacity: int):
        self.size = capacity
        self.head = None
        self.tail = None
        #so the least recently used val is the head
        #and the last used is the right
        self.dict = {}
        self.count = 0
    
    def toTheEnd(self, node : NodeList):

        #this function send a node at the time
        #the node can be created for the first time or not it will be perfectly linked

        if not self.head:
            self.head = node
        elif node == self.head and not self.tail:
            return
        elif not self.tail:
            self.tail = node
            self.head.next = node
            node.prev = self.head
        elif node != self.tail:
            if (node == self.head):
                self.head = self.head.next
                if (self.head):
                    self.head.prev = None
            prev_tmp = node.prev
            next_tmp = node.next
            if (next_tmp):
                next_tmp.prev = prev_tmp
            if (prev_tmp):
                prev_tmp.next = next_tmp
            node.prev = self.tail
            self.tail.next = node
            node.next = None
            self.tail = node

    def get(self, key: int) -> int:
        if key in self.dict:
            self.toTheEnd(self.dict[key])
            return (self.dict[key].val)
        else:
            return (-1)

    def put(self, key: int, value: int) -> None:
        if (key in self.dict):
            self.dict[key].val = value
            self.toTheEnd(self.dict[key])
        elif (self.count < self.size):
            node = self.NodeList(key, value)
            self.dict[key] = node
            self.toTheEnd(node)
            self.count +=1
        else:
            evict = self.head
            del self.dict[evict.key]
            evict.key = key
            evict.val = value
            self.dict[key] = evict
            self.head = evict.next
            self.toTheEnd(evict)



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