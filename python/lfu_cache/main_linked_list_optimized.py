#!/usr/bin/env python3

from os import remove

class LFUCache:

    class NodeList:

        def __init__(self, key, val, prev=None, nextt=None) -> None:
            self.key = key
            self.val= val
            self.counter = 1
            self.prev = prev
            self.next = nextt
            pass

    
    def puta(self, key, val):
        pass
        
    def geta(self, key):
        return (-1)

    def __init__(self, capacity: int):
        self.size = capacity
        self.head = None
        self.tail = None
        #je dois créer un dictionaire qui contient le dernier element de chaque counter
        #je devrai faire find dans values de l'index 

        #so the least recently used val is the head
        #and the last used is the right
        self.dict = {}
        self.count = 0
        if (capacity == 0):
            self.put = self.puta
            self.get = self.geta
    
    def toTheEnd(self, node : NodeList, refe : NodeList):

        #this function send a node at the time
        #the node can be created for the first time or not it will be perfectly linked

        if not self.head:
            self.head = node
        elif node == self.head and not self.tail:
            return
        elif node != self.tail:
            tmp_next = node.next
            tmp_prev = node.prev
            extract = None
            while refe and node.counter >= refe.counter:
                extract = refe
                refe = refe.next
            if (extract):
                tmp_extract_next = extract.next
                extract.next = node
                node.prev = extract
                node.next = tmp_extract_next
                if (tmp_extract_next):
                    tmp_extract_next.prev = node
                if (node.next == None):
                    self.tail = node
                if (tmp_prev):
                    tmp_prev.next = tmp_next
                else:
                    self.head = tmp_next if tmp_next else self.head
                if (tmp_next):
                    tmp_next.prev = tmp_prev
            else:
                if node.prev == None:
                    self.head.prev = node
                    node.next = self.head
                    self.head = node

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            node.counter += 1
            self.toTheEnd(node, node.next)
            return (node.val)
        else:
            return (-1)

    def put(self, key: int, value: int) -> None:
        if (key in self.dict):
            node = self.dict[key]
            self.dict[key].val = value
            node.counter += 1
            self.toTheEnd(node, node.next)
        elif (self.count < self.size):
            node = self.NodeList(key, value)
            self.dict[key] = node
            self.toTheEnd(node, self.head)
            self.count +=1
        else:
            evict = self.head
            del self.dict[evict.key]
            evict.key = key
            evict.val = value
            self.dict[key] = evict
            evict.counter = 1
            self.toTheEnd(evict, self.head)
    def p(self):
        print("head = ", self.head, "tail = ", self.tail)
        for i in self.dict.values():
            print("key",i.key, "val",i.val, "count",i.counter)




# Your LRUCache object will be instantiated and called as such:
obj = LFUCache(0)
obj.put(1,1)
obj.p()
obj.put(2,2)
obj.p()
print(obj.get(1))
obj.put(3,3)
print(obj.get(2))
print(obj.get(3))
obj.put(4,4)
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))
obj.put(1,1)
obj.put(4,1)

print("last")
a = LFUCache(10)
a.put(10,13)
a.put(3,17)
a.put(6,11)
a.put(10,5)
a.put(9,10)
print(a.get(13))
a.put(2,19)
print(a.get(2))
print(a.get(3))
a.put(5,25)
print(a.get(8))
a.put(9,22)
a.put(5,5)
a.put(1,30)
print(a.get(11))
a.put(9,12)
print(a.get(7))
print(a.get(5))
print(a.get(8))
print(a.get(9))
a.put(4,30)
a.put(9,3)
print(a.get(9))
print(a.get(10))
print(a.get(10))

a.put(6,14)
a.put(3,1)
print(a.get(3))
a.put(10,11)
print(a.get(8))

a.put(2,14)
print(a.get(1))
print(a.get(5))
print(a.get(4))
a.put(11,4)
a.put(12,24)
a.put(5,18)
print(a.get(13))

a.put(7,23)
print(a.get(8))
print(a.get(12))

a.put(3,27)
a.put(2,12)
print(a.get(5))

a.put(2,9)
a.put(13,4)
a.put(8,18)
a.put(1,7)
print(a.get(6))

a.put(9,29)
a.put(8,21)
print(a.get(5))
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
a.put()
#print(a.get())

# param_1 = obj.get(key)
# obj.put(key,value)