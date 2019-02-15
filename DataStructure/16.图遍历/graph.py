from collections import deque

GRAPH = {
    'A': ['B', 'F'],
    'B': ['C', 'I', 'G'],
    'C': ['B', 'I', 'D'],
    'D': ['C', 'I', 'G', 'H', 'E'],
    'E': ['D', 'H', 'F'],
    'F': ['A', 'G', 'E'],
    'G': ['B', 'F', 'H', 'D'],
    'H': ['G', 'D', 'E'],
    'I': ['B', 'C', 'D'],
}

class Quene(object):

    def __init__(self):
        self._deque = deque()

    def push(self, value):
        return self._deque.append(value)

    def pop(self):
        return self._deque.popleft()

    def __len__(self):
        return len(self._deque)

def bfs(graph,start):
    search_quene = Quene()
    search_quene.push(start)
    searched = set()
    while search_quene:
        cur_node = search_quene.pop()
        if cur_node not in searched:
            searched.add(cur_node)
            print(cur_node)
            for node in graph[cur_node]:
                search_quene.push(node)

DFS_SEARCHED = set()

def dfs(graph,start):
    if start not in DFS_SEARCHED:
        print(start)
        DFS_SEARCHED.add(start)
    for node in graph[start]:
        if node not in DFS_SEARCHED:
            dfs(graph,node)

print('bfs:')
bfs(GRAPH,'A')
print('*'*10)
print('dfs:')
dfs(GRAPH,'A')