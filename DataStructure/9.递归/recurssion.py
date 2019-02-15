from collections import deque

def fact(n):
    if n == 0: #递归出口
        return 1
    else:
        n = n * fact(n-1) #向递归出口靠近
        return n 

def print_num_recursion(n):
    
    if n > 0:
        print_num_recursion(n-1)
        print(n)
        
class Stack(object):

    def __init__(self):
        self.deque = deque()

    def push(self,value):
        return self.deque.append(value)

    def pop(self):
        return self.deque.pop()

    def is_empty(self):
        return len(self.deque) == 0


def print_num_use_stack(n):
    s = Stack()
    while n > 0:
        s.push(n)
        n -= 1

    while not s.is_empty():
        print(s.pop())

#print_num_use_stack(10)

def hanoi_move(n, source, desti, intermediate):
    if n >=1 : #递归出口，只剩下一个盘子
        hanoi_move(n-1, source, intermediate, desti)
        print("move %s -> %s" % (source, desti))
        hanoi_move(n-1, intermediate, desti, source)
hanoi_move(5,'A','B','C')
