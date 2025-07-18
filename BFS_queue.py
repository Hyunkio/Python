from collections import deque

def bfs(graph, start): #graph, 'A' 시작
    visited = []
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited

graph = {
    'A' : ['B', 'C'],
    'B' : ['A', 'D', 'E'],
    'C' : ['A', 'F'],
    'D' : ['B'],
    'E' : ['B', 'F'],
    'F' : ['C', 'E']
}

print(bfs(graph, 'A'))