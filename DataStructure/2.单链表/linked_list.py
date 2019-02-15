# -*- coding: utf-8 -*-
class Node(object):

    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next

class LinkedList(object):
    """ 链接表 ADT
    [root] -> [node0] -> [node1] -> [node2]
    """

    def __init__(self,maxsize=None):
        """
        :param maxsize: int or None, 如果是 None，无限扩充
        """
        self.root = Node()
        self.tailnode = None
        self.length = 0
        self.maxsize = maxsize
    
    def __len__(self):
        return self.length


    def append(self,value): #O(1)
        if len(self) > self.maxsize and self.maxsize is not None:
            raise Exception("full error")
        node = Node(value)
        tailnode = self.tailnode
        if self.tailnode == None:
            self.root.next = node
        else:
            tailnode.next = node
        self.length += 1
        self.tailnode = node



    def appendleft(self,value): #O(1)
        headnode = self.root.next
        node = Node(value)
        self.root.next = node
        node.next = headnode
        self.length += 1

    def iter_node(self):
        """遍历 从 head 节点到 tail 节点"""
        currnode = self.root.next
        while currnode is not self.tailnode:
            yield currnode
            currnode = currnode.next
        yield currnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value


    def find(self, value):
        """ 查找一个节点，返回序号，从 0 开始
        :param value:
        """
        index = 0
        for node in self.iter_node():
            if node.value == value:
                return index
            index += 1
        return -1 #返回-1用来标示

    def clear(self): #O(n) 
        for node in self.iter_node():
            del node
        self.root.next = None
        self.length = 0


    def remove(self,value): #O(n)
        """ 删除包含值的一个节点，将其前一个节点的 next 指向被查询节点的下一个即可
        :param value:
        """
        prenode = self.root
        currnode = self.root.next
        for currnode in self.iter_node():
            if currnode.value == value:
                prenode.next = currnode.next
                if currnode is self.tailnode: #NOTES:update the tailnode
                    self.tailnode = prenode
                del currnode
                self.length -= 1
                return 1
            else:
                prenode = currnode
        return -1


    def popleft(self): #O(1)
        if self.root.next == None:
            raise Exception('pop from empty')
        headnode = self.root.next
        self.root.next = headnode.next
        self.length -= 1
        value = headnode.value
        del headnode
        return value




def test_linked_list():
    ll = LinkedList()

    ll.append(0)
    ll.append(1)
    ll.append(2)

    assert len(ll) == 3
    assert ll.find(3) == -1
    ll.remove(0)
    assert len(ll) == 2
    assert ll.find(0) == -1

    assert list(ll) == [1, 2]

    ll.appendleft(0)
    assert list(ll) == [0,1,2]
    assert len(ll) == 3

    headvalue = ll.popleft()
    assert headvalue == 0
    assert len(ll) == 2
    assert list(ll) == [1, 2]

    ll.clear()
    assert len(ll) == 0

if __name__ == '__main__':
    test_linked_list()
    test_linked_list_append()
    test_linked_list_reverse()

    
