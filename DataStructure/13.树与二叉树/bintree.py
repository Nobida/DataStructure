# -*- coding: utf-8 -*-
#根节点，路径，父亲，孩子，兄弟，子树，叶子节点

#每个节点只能包含两个孩子
#满二叉树 完美二叉树 完全二叉树

node_list = [
    {'data': 'A', 'left': 'B', 'right': 'C', 'is_root': True},
    {'data': 'B', 'left': 'D', 'right': 'E', 'is_root': False},
    {'data': 'D', 'left': None, 'right': None, 'is_root': False},
    {'data': 'E', 'left': 'H', 'right': None, 'is_root': False},
    {'data': 'H', 'left': None, 'right': None, 'is_root': False},
    {'data': 'C', 'left': 'F', 'right': 'G', 'is_root': False},
    {'data': 'F', 'left': None, 'right': None, 'is_root': False},
    {'data': 'G', 'left': 'I', 'right': 'J', 'is_root': False},
    {'data': 'I', 'left': None, 'right': None, 'is_root': False},
    {'data': 'J', 'left': None, 'right': None, 'is_root': False},
]

class BinTreeNode(object):
    
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

class BinTree(object):

    def __init__(self,root=None):
        self.root = root

    @classmethod
    def build_from(cls,node_list):
        node_dict = {}
        for node_data in node_list:
            data = node_data['data']
            node_dict[data] = BinTreeNode(data)
        for node_data in node_list:
            data = node_data['data']
            node = node_dict[data]
            if node_data['is_root']:
                root = node
            node.left = node_dict.get(node_data['left'])
            node.right = node_dict.get(node_data['right'])
        return cls(root)



    def preorder_trav(self, subtree):
        if subtree is not None:
            print(subtree)
            print(subtree.data)
            self.preorder_trav(subtree.left)
            self.preorder_trav(subtree.right)

    def reverse(self,subtree):
        if subtree is not None:
            subtree.left, subtree.right = subtree.right = subtree.left
            self.reverse(subtree.left)
            self.reverse(subtree.right)
    




btree = BinTree.build_from(node_list)
print('====先序遍历=====')
btree.preorder_trav(btree.root)
































class BinTreeNode(object):

    def __init__(self,data,left=None,right=None):
        self.data = data
        self.left = left
        self.right = right

class BinTree(object):

    def __init__(self,root=None):
        #根节点设置
        self.root = root

    @classmethod
    def build_from(cls,node_list):
        node_dict = {}
        for node_data in node_list:
            data = node_data['data']
            node_dict[data] = BinTreeNode(data)
        for node_data in node_list:
            data = node_data['data']
            node = node_dict[data]
            if node_data['is_root']:
                root = node
            node.left = node_dict.get(node_data['left'])
            node.right = node_dict.get(node_data['right'])

        return cls(root)

    def preorder_trav(self, subtree):
        if subtree is not None:
            print(subtree.data)
            self.preorder_trav(subtree.left)
            self.preorder_trav(subtree.right)

    def reverse(self,subtree):
        if subtree is not None:
            subtree.left, subtree.right = subtree.right,subtree.left
            self.reverse(subtree.left)
            self.reverse(subtree.right)

btree = BinTree.build_from(node_list)
print('====先序遍历=====')
btree.preorder_trav(btree.root)



btree.reverse(btree.root)
print('====反转之后的结果=====')
btree.preorder_trav(btree.root)

