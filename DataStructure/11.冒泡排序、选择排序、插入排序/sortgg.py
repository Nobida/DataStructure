import random

def bubble_sort(iterable):
    _len = len(iterable)
    for i in range(len(iterable)-1):
        for j in range(len(iterable)-1-i):
            if iterable[j] > iterable[j+1]:
                iterable[j+1],iterable[j] = iterable[j],iterable[j+1]
    return iterable


def select_sort(iterable):
    _len = len(iterable)
     
    for i in range(_len):
        min_pos = i #假设当前下标的值最小
        for j in range(i+1, _len):
            if iterable[j] < iterable[min_pos]:
                min_pos = j
        if i != min_pos:
            iterable[i],iterable[min_pos] = iterable[min_pos],iterable[i]

    return iterable

def insertion_sort(seq):
    """ 每次挑选下一个元素插入已经排序的数组中,初始时已排序数组只有一个元素"""
    n = len(seq)
    print(seq)
    for i in range(1, n):
        value = seq[i]    # 保存当前位置的值，因为转移的过程中它的位置可能被覆盖
        print("######")
        print(value)
        # 找到这个值的合适位置，使得前边的数组有序 [0,i] 有序
        pos = i
        print(pos)
        while pos > 0 and value < seq[pos-1]:
            seq[pos] = seq[pos-1]  # 如果前边的元素比它大，就让它一直前移
            pos -= 1
        seq[pos] = value    # 找到了合适的位置赋值就好
        print(seq)

insertion_sort([0,8,6,4,2])






def insert_sort(seq):
    for i in range(seq):
        value = seq[i]
        pos = i
        while pos < 0 and value < seq[i-1]:
            seq[pos] = seq[pos-1]
            pos -= 1
        seq[pos] = value  


def test_bubble_sort():
    list_ = [i for i in range(50)]
    random.shuffle(list_)
    list1 = bubble_sort(list_)
    list2 = sorted(list_)
    assert list1 == list2 



def test_select_sort():
    list_ = [i for i in range(50)]
    random.shuffle(list_)
    list1 = select_sort(list_)
    list2 = sorted(list_)
    assert list1 == list2 

def test_insert_sort():
    list_ = [i for i in range(50)]
    random.shuffle(list_)
    list1 = insert_sort(list_)
    list2 = sorted(list_)
    assert list1 == list2 

if __name__ == "__main__":
    test_bubble_sort()
    test_select_sort()
    test_insert_sort()


    

