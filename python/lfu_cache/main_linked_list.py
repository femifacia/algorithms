#!/usr/bin/env python3

from os import remove

class LFUCache:

    class NodeList:

        def __init__(self, key, val, index = 0, prev=None, nextt=None) -> None:
            self.key = key
            self.val= val
            self.counter = 1
            self.index = index
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
        self.counter_max = 0
        self.dict_counter_nbr = {}
        self.dict_counter = {}
        self.count = 0
        if (capacity == 0):
            self.put = self.puta
            self.get = self.geta

    def removeNode(self, node : NodeList):
        if (node != self.tail):
            if (node.prev):
                node.prev.next = node.next
            if (node.next):
                node.next.prev = node.prev
            if (node == self.head and node.next and self.head.counter >= node.next.counter):
                self.head = node.next
        self.dict_counter_nbr[node.counter] -= 1
        if (self.dict_counter_nbr[node.counter] == 0):
            del self.dict_counter_nbr[node.counter]
            del self.dict_counter[node.counter]

    def findPredecessor(self, node : NodeList) -> NodeList:
        idx = node.counter
        while (idx > 0  and (idx not in self.dict_counter)):
            idx -= 1
        return (self.dict_counter[idx] if idx > 0 else None)

    def findSuccessor(self, node : NodeList) -> NodeList:
        idx = node.counter + 1
        while (idx < self.tail.counter  and (idx not in self.dict_counter)):
            idx -= 1
        return (self.dict_counter[idx] if idx < self.counter_max else None)

    def addNode(self, node : NodeList) -> None:
        if not self.head:
            self.head = node
            self.dict_counter[node.counter] = node
            self.dict_counter_nbr[node.counter] = 1
            self.counter_max = 1
        elif not self.tail:
            successor = self.findSuccessor(node)
            if (successor):
                self.tail = successor
                self.head = node
                self.tail.prev = self.head
                self.dict_counter[node.counter] = node
                self.dict_counter_nbr[node.counter] = 1
                self.counter_max = self.tail.counter
            else:
                self.tail = node
                node.prev = self.head
                self.head.next = node
                self.dict_counter[node.counter] = node
                self.dict_counter_nbr[node.counter] += 1
        else:
            successor = self.findSuccessor(node)
            predecessor = self.findPredecessor(node)
            if (not predecessor and successor):
                self.head = 
            self.dict_
            self.head.next = node
            node.prev = self.head



    def toTheEnd(self, node : NodeList, refe : NodeList):

        #this function send a node at the time
        #the node can be created for the first time or not it will be perfectly linked

        if not self.head:
            self.head = node
        elif not tail and node != self.head:
            self.tail = node
        if not node.counter in self.dict_counter :
            self.dict_counter[node.counter] = node
            self.dict_counter_nbr[node.counter] = 1

            

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