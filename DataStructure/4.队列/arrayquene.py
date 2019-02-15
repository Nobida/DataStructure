# -*- coding: utf-8 -*-



class Array(object):
    def __init__(self,size=32):
        self._size = size
        self._items = [None] * size

    def __getitem__(self, index):
        #魔术方法，通过它实现括号访问
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self._size

    def clear(self,value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item


class FullError(Exception):
    pass

class EmptyError(Exception):
    pass



class ArrayQuene(object):

    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.head = 0
        self.tail = 0
        self.array = Array(maxsize)
    
    def push(self,value):
        if len(self) >= self.maxsize:
            raise FullError("full error")
        self.array[self.head % self.maxsize] = value
        self.head += 1

    def pop(self):
        if len(self) == 0:
            raise EmptyError('empty')
        value = self.array[self.tail % self.maxsize]
        self.tail += 1
        return value

    def __len__(self):
        return self.head - self.tail

def test_queue():
    import pytest    # pip install pytest
    size = 5
    q = ArrayQuene(size)
    for i in range(size):
        q.push(i)

    with pytest.raises(FullError) as excinfo:   # 我们来测试是否真的抛出了异常
        q.push(size)
    assert 'full' in str(excinfo.value)

    assert len(q) == 5

    assert q.pop() == 0
    assert q.pop() == 1

    q.push(5)

    assert len(q) == 4

    assert q.pop() == 2
    assert q.pop() == 3
    assert q.pop() == 4
    assert q.pop() == 5

















