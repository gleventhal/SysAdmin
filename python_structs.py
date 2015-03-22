#!/usr/bin/env python

class Stack(object):
    '''Creates a stack object'''
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1::] 
        
    def size(self):
        return len(self.items)

class Queue(object):
    '''Creates a queue object'''
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        i = self.items[0]
        del(self.items[0])
        return i

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]


