from collections import deque
from collections import defaultdict

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E', 'F'],
    'C': ['G'],
    'D': [],
    'E': [],
    'F': ['H'],
    'G': ['I'],
    'H': [],
    'I': []
}


def bfs(graph, root):
    visited = defaultdict()
    queue = deque(root)

    while queue:
        currVert = queue.popleft()
        print(graph[currVert])

        for vert in graph[currVert]:
            if vert not in visited:
                visited[vert] = 0
                queue.append(vert)


if __name__ == "__main__":
    bfs(graph, "A")
