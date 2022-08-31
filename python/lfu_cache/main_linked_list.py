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
        self.dict = {}
        self.counter_max = 0
        self.dict_counter_nbr = {}
        self.dict_counter_head = {}
        self.dict_counter_tail = {}
        self.count = 0
        if (capacity == 0):
            self.put = self.puta
            self.get = self.geta

    def addNode(self, node : NodeList, evict_next = None) -> None:
        if not self.head:
            self.head = node
            self.dict_counter_head[node.counter] = node
            self.dict_counter_tail[node.counter] = node
            self.dict_counter_nbr[node.counter] = 1
            self.counter_max = 1
        elif not 1 in self.dict_counter_head:
            node.next = self.head if evict_next == None else evict_next
            self.head.prev = node
            self.head = node
            node.prev = None
            self.dict_counter_head[node.counter] = node
            self.dict_counter_tail[node.counter] = node
            self.dict_counter_nbr[node.counter] = 1
        else:
            tmp_prev = self.dict_counter_tail[1]
            tmp_next = tmp_prev.next
            tmp_prev.next = node
            node.prev = tmp_prev
            node.next = tmp_next
            if (tmp_next):
                tmp_next.prev = node
            self.dict_counter_nbr[1] += 1
            self.dict_counter_tail[1] = node
    
    def incrCounterNode(self, node : NodeList) -> None:
        tmp_prev = node.prev
        tmp_next = node.next
#        if node.key == 2:
#            print("montmp", tmp_prev.val)
        old_counter = node.counter
        node.counter += 1
        self.dict_counter_nbr[old_counter] -= 1
        if not node.counter in self.dict_counter_head:
            self.dict_counter_head[node.counter] = node
            self.dict_counter_tail[node.counter] = node
            self.dict_counter_nbr[node.counter] = 1
            if self.dict_counter_nbr[old_counter] <= 0:
                del self.dict_counter_nbr[old_counter]
                del self.dict_counter_head[old_counter]
                del self.dict_counter_tail[old_counter]
                return
            if (self.dict_counter_tail[old_counter] == node):
                self.dict_counter_tail[old_counter] = tmp_prev
                return
            if (self.dict_counter_head[old_counter] == node):
                self.dict_counter_head[old_counter] = self.dict_counter_head[old_counter].next
                if (tmp_prev):
                    tmp_prev.next = self.dict_counter_head[old_counter]
                self.dict_counter_head[old_counter].prev = tmp_prev
                if (tmp_next.next == None):
                    tmp_next.next = node
                    node.next = None
                if (node == self.head):
                    self.head = self.dict_counter_head[old_counter]
                    self.head.prev = None
                new_prev = self.dict_counter_tail[old_counter]
                new_next = new_prev.next
                new_prev.next = node
                node.next = new_next
                if (new_next):
                    new_next.prev = node
                return
            tmp_prev.next = tmp_next
            tmp_next.prev = tmp_prev
            new_prev = self.dict_counter_tail[old_counter]
            new_next = new_prev.next
            new_prev.next = node
            node.next = new_next
            if (new_next):
                new_next.prev = node
        else:
            new_prev = self.dict_counter_tail[node.counter]
            new_next = new_prev.next
            new_prev.next = node
            node.prev = new_prev
            node.next = new_next
            if (new_next):
                new_next.prev = node
            self.dict_counter_nbr[node.counter] += 1
            self.dict_counter_tail[node.counter] = node
            if (self.dict_counter_nbr[old_counter] <= 0):
                del self.dict_counter_nbr[old_counter]
                del self.dict_counter_head[old_counter]
                del self.dict_counter_tail[old_counter]
                if (tmp_prev):
                    tmp_prev.next = tmp_next
                if (tmp_next):
                    tmp_next.prev = tmp_prev
                if (self.head == node):
#                    self.print
#                    self.p()
                    #print(self.head == tmp_next)
                    #print("llllllllllllllllllllllll", tmp_next.key, tmp_next.val, "\n\n\n\n\n")
                    self.head = self.dict_counter_head[node.counter]
                    #print("lololololo", tmp_next.val)
                return
            if (self.dict_counter_head[old_counter] == node):
                self.dict_counter_head[old_counter] = tmp_next
                if (tmp_prev):
                    tmp_prev.next = tmp_next
                tmp_next.prev = tmp_prev
                if (tmp_next.next == None):
                    tmp_next.next = self.dict_counter_head[node.counter]
                    self.dict_counter_head[node.counter].next = None
                if (self.head == node):
                    self.head = self.dict_counter_head[old_counter]
                return
            if (self.dict_counter_tail[old_counter] == node):
                self.dict_counter_tail[old_counter] = tmp_prev
                tmp_prev.next = self.dict_counter_head[node.counter]
                self.dict_counter_head[node.counter].prev = tmp_prev
                return
            tmp_prev.next = tmp_next
            tmp_next.prev = tmp_prev
    
    def evict(self, node : NodeList) -> None:
        tmp_next = node.next
        #print("veictttttttt", node.counter)
        self.dict_counter_nbr[node.counter] -= 1
        if (self.dict_counter_nbr[node.counter] <= 0):
            del self.dict_counter_head[node.counter]
            del self.dict_counter_tail[node.counter]
            del self.dict_counter_nbr[node.counter]
        else:
            self.dict_counter_head[node.counter] = self.dict_counter_head[node.counter].next
            self.head = self.dict_counter_head[node.counter]
            self.head.prev = None
            #print("shalom", self.head.val)
        node.prev = None
        node.next = None
        node.counter = 1
        self.addNode(node, tmp_next)
            

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            self.incrCounterNode(node)
            return (node.val)
        else:
            return (-1)

    def put(self, key: int, value: int) -> None:
        if (key in self.dict):
            node = self.dict[key]
            self.dict[key].val = value
            self.incrCounterNode(node)
        elif (self.count < self.size):
            node = self.NodeList(key, value)
            self.dict[key] = node
            self.addNode(node)
            self.count +=1
        else:
            evict = self.head
            del self.dict[evict.key]
            evict.key = key
            evict.val = value
            self.dict[key] = evict
            self.evict(evict)
    def p(self):
        if (self.head and self.tail):
            print("head = ", self.head.val, "tail = ", self.tail.val)
        elif (self.head):
            print("head = ", self.head.val, "tail = ", self.tail)

        elif (self.tail):
            print("head = ", self.head, "tail = ", self.tail.val)

        else:
            print("head = ", self.head, "tail = ", self.tail)            
        for i in self.dict.values():
            print("key",i.key, "val",i.val, "count",i.counter)
        for i in self.dict_counter_head:
            print("at, i", i, "head = ", self.dict_counter_head[i].val, "tail =", self.dict_counter_tail[i].val)
        print("end printing\n")

    def printList(self):
        node = self.head
        while (node):
            print("key = ",node.key, "val =", node.val, end="->")
            node = node.next
        print("")



# Your LRUCache object will be instantiated and called as such:


test = [[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]

first = LFUCache(10)
for i in range(len(test)):
    if len(test[i]) == 2:
        first.put(test[i][0], test[i][1])
    else:
        print (first.get(test[i][0]), "at i = ", i)
    if (i < 7):
        print("op", test[i])
        first.printList()
#print("check",first.head.prev.val)