from collections import deque

class DoublyLinkedList(object):
    def __init__(self):
        self.h=deque([])

    def push(self,x):
        self.h.append(x)

    def unshift(self,x):
        self.h.appendleft(x)

    def pop(self):
        return self.h.pop()

    def shift(self):
        return self.h.popleft()