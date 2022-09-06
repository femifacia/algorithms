#!/usr/bin/python3.8

class ourQueue:
    def __init__(self):
        self.in_stack = [] #the tail
        self.out_stack = [] #the head
        
    def push(self, obj):
        self.in_stack.append(obj)

    def pop(self):
        if (not self.out_stack):
            self.out_stack = self.in_stack[::-1]
            self.in_stack = []
        return (self.out_stack.pop())

    def __len__(self):
        return (len(self.in_stack) + len(self.out_stack))
    
    def __str__(self):
        return " ".join(str(i) for i in self.in_stack) + " ".join(str(i) for i in self.out_stack)
    
var = ourQueue()
var.push("sah")
var.push("marche")
var.push("le_last")
var.push(5)
var.push([5,9])
print(str(var))
print(var.pop())
print(var.pop())
print(str(var))
