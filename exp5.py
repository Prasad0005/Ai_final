
from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

q = deque([('A', ['A'])])
visited = set()

while q:
    node, path = q.popleft()

    if node == 'G':
        print("Path:", path)
        break

    if node not in visited:
        visited.add(node)

        for next_node in graph[node]:
            q.append((next_node, path + [next_node]))
