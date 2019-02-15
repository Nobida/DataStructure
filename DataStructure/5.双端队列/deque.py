# -*- coding: utf-8 -*-



class Node(object):

    def __init__(self,next=None,pre=None,value=None):
        self.value = value
        self.next = next
        self.pre = pre
        

class CirculDoubledLinkeList(object):

    def __init__(self,maxsize=None):
        self.maxsize = maxsize
        self.length = 0
        node = Node()
        self.root = node
        node.prev = node
        node.next = node

    def __len__(self):
        return self.length

    def headnode(self):
        return self.root.next

    def tailnode(self):
        return self.root.prev



    def append(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception("full error")
        node = Node(value=value)
        tailnode = self.tailnode()
        tailnode.next = node
        node.prev = tailnode
        node.next = self.root
        self.root.prev = node
        self.length += 1

    def appendleft(self,value):
        if len(self) > self.maxsize and self.maxsize is not None:
            raise Exception("full")
        node = Node(value=value)

        if self.root.next is self.root:
            self.root.next = node
            self.root.prev = node
            node.prev = self.root
            node.next = self.root
        else:
            headnode = self.root.next
            self.root.next = node
            node.next = headnode
            headnode.prev = node
            node.prev = self.root
        self.length += 1

    def remove(self,node):
        if self.root.next is self.root:
            raise Exception("no node to remove")
        node.prev.next = node.next
        node.next.prev = node.prev
        #del node
        self.length -= 1
        return node

    def iter_node(self):
        if self.root.next is self.root:
            return 
        currnode = self.root.next
        while currnode.next is not self.root:
            yield currnode
            currnode = currnode.next
        yield currnode
        

    def __iter__(self):
        for node in self.iter_node():
            yield node

    def iter_node_reverse(self):
        if self.root.prev is self.root:
            return 
        currnode = self.root.prev
        while currnode.prev is not self.root:
            yield currnode
            currnode = currnode.prev
        yield currnode


class FullError(Exception):
    pass

class EmptyError(Exception):
    pass

class Dequene(CirculDoubledLinkeList):

    def pop(self):
        if len(self) == 0:
            raise EmptyError('empty')
        tailnode = self.tailnode()
        self.remove(tailnode)
        return tailnode.value

    def popleft(self):
        if len(self) == 0:
            raise EmptyError('empty')
        headnode = self.tailnode()
        self.remove(headnode)
        return headnode.value

def test_dequene():
    
    d = Dequene()
    d.append(0)

    assert d.pop() == 0
        