number_list = [1,1,2,3,4,5,6,7]

#线性查找就是从头找到尾，直到符合条件就返回
def linear_search(value, iterable):
    for index, val in enumerate(iterable):
        if val == value:
            return index
        return -1

def jiecheng(n):
    if n == 0:
        return 1
    else:
        return n*jiecheng(n)

def linear_search_recursive(value,index,iterable):
    found = False
    while not found:
        if len(iterable) == 0 or index > len(iterable)-1:
            return False
            break
        if iterable[index] == value:
            found = True
            return index
        else:
            index += 1
            linear_search_recursive(value,index,iterable)


def linear_search_recursive(value,iterable):
    if len(iterable) == 0:
        return -1
    index = len(iterable) - 1
    if iterable[index] == value:
        return value
    else:
        return linear_search(value,iterable[0:index])
    




#但若一个序列已经是有序的
def binary_search(sorted_array, val):
    if sorted(sorted_array) != sorted_array:
        return -1
    start = 0
    end = len(sorted_array) - 1
    while start <= end:
        #print(end)
        mid = int((start + end) / 2)
        #print(mid)
        #print(sorted_array[mid])
        if sorted_array[mid] == val:
            return mid
        elif sorted_array[mid] > val: 
            end = mid - 1
        else:
            start = mid + 1
    return - 1

def binary_search_recursive(sorted_array,start,end,val):
    if sorted(sorted_array) != sorted_array:
        return -1
    if start >= end:
        return -1
    mid = (start + end) // 2
    print(mid)
    if sorted_array[mid] == val:
        return mid
    elif sorted_array[mid] > val:
    
        return binary_search_recursive(sorted_array,start,mid,val)
    else:
        start = mid + 1
        return binary_search_recursive(sorted_array,start,end,val)

def test_binary_search_recursive():
    # 我们测试所有值和边界条件
    a = list(range(10))
    print(a)
    #for i in a:
    print(binary_search_recursive(a, 0, len(a), 1))

    assert binary_search_recursive(a, 0, len(a), -1) == -1
    assert binary_search_recursive(a, 0, len(a), 10) == -1


def test_binary_search():
    a = list(range(10))
    for i in a:
        assert binary_search(a, i) == i
    assert binary_search(a, -1) == -1
    

test_binary_search_recursive()





