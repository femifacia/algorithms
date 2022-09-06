#!/usr/bin/env python3

class myHeap:
    def __init__(self) -> None:
        self.heap = [None]
        self.rank = {}
        self.size = 1

    def __len__(self) -> int:
        return (self.size - 1)

    def up(self, i) -> None:
        elm =self.heap[i]
        while i > 1 and elm < self.heap[i // 2]:
            self.heap[i] = self.heap[i // 2]
            self.rank[self.heap[i // 2]] = i
            i //= 2
        self.heap[i] = elm
        self.rank[elm] = i

    def push(self, elm):
        assert (elm not in self.heap)
        self.heap.append(elm)
        self.rank[elm] = self.size
        self.up(self.size)
        self.size += 1

    def down(self, i) -> None:
        elm = self.heap[i]
        limit = len(self.heap)
        while 1:
            left_son = 2*i
            right_son = 2*i + 1
            if (right_son < limit and elm > self.heap[right_son] and self.heap[right_son] < self.heap[left_son]):
                self.heap[i] = self.heap[right_son]
                self.rank[self.heap[right_son]] = i
                i = right_son
            elif left_son < limit and elm > self.heap[left_son]:
                self.heap[i] = self.heap[left_son]
                self.rank[self.heap[left_son]] = i
                i = left_son
            else:
                self.heap[i] = elm
                self.rank[elm] = i
                return

    def pop(self) -> int:
        root = self.heap[1]
        last = self.heap.pop()
        self.size -= 1
        if (self):
            self.heap[1] = last
            self.rank[last] = 1
            self.down(1)
        del self.rank[root]
        return (root)

    def update(self, old, new):
        old_index = self.rank[old]
        del self.rank[old]
        self.heap[old_index] = new
        self.rank[new] = old_index
        if (new > old):
            self.down(old_index)
        else:
            self.up(old_index)

    def __str__(self) -> str:
        return (str(self.heap))