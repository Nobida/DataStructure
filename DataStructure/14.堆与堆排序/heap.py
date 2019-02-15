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


class MaxHeap(object):

    def __init__(self,maxsize=None):
        self.maxsize = maxsize
        self._elements = Array(maxsize)
        self._count = 0

    def __len__(self):
        return self._count

    def add(self,value):
        if self._count >= self.maxsize:
            raise Exception('full')
        self._elements[self._count] = value
        self._count += 1
        self._siftup(self._count - 1)



    def _siftup(self,ndx):
        if ndx > 0:
            parent = int((ndx-1)/2)
            if self._elements[ndx] > self._elements[parent]:
                self._elements[parent],self._elements[ndx] = self._elements[ndx],self._elements[parent]
                self._siftup(parent)



    def extract(self):
        if self._count <= 0:
            raise Exception('empty')
        value = self._elements[0]
        self._count -= 1
        self._elements[0] = self._elements[self._count]
        self._siftdown(0)
        return value

    def _siftdown(self,ndx):
        left = 2*ndx+1
        right = 2*ndx+2
        largest = ndx

        if (self._count > left and
            self._elements[left] > self._elements[ndx] and 
            self._elements[left] > self._elements[right]):
            largest = left
        elif (self._count > right and 
            self._elements[right] > self._elements[ndx] and
            self._elements[right] > self._elements[left]):
            largest = right
        if largest != ndx:
            self._elements[largest],self._elements[ndx] = self._elements[ndx],self._elements[largest]
            self._siftdown(largest)

class PriorityQuene(object):

    def __init__(self,maxsize):
        self.maxsize = maxsize
        self._maxheap = MaxHeap(maxsize)

    def push(self,priority,value):
        entry = (priority,value)
        self._maxheap.add(entry)

    
    def pop(self, with_priority = False):
        entry = self._maxheap.extract()
        if with_priority:
            return entry
        else:
            return entry[1]
        

    def is_empty(self):
        return len(self._maxheap) ==0

def test_priority_queue():
    size = 5
    pq = PriorityQuene(size)
    pq.push(5, 'purple')
    pq.push(0, 'white')
    pq.push(3, 'orange')
    pq.push(1, 'black')

    res = []
    while not pq.is_empty():
        res.append(pq.pop())
    print(res)
    assert res == ['purple', 'orange', 'black', 'white']
test_priority_queue()


        


        











