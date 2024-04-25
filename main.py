from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    # Priority queue for Dijkstra's algorithm
    queue = [(0, 0, source)]  # (weight, edges, vertex)
    distances = {vertex: float('infinity') for vertex in graph}
    edges_count = {vertex: float('infinity') for vertex in graph}
    shortest_paths = {}

    distances[source] = 0
    edges_count[source] = 0

    while queue:
        weight, edges, current = heappop(queue)

        if current not in shortest_paths:
            shortest_paths[current] = (weight, edges)

            for neighbor, neighbor_weight in graph[current]:
                total_weight = weight + neighbor_weight
                total_edges = edges + 1
                if total_weight < distances[neighbor] or (total_weight == distances[neighbor] and total_edges < edges_count[neighbor]):
                    distances[neighbor] = total_weight
                    edges_count[neighbor] = total_edges
                    heappush(queue, (total_weight, total_edges, neighbor))

    return shortest_paths

def bfs_path(graph, source):
    queue = deque([source])
    parents = {source: None}

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if neighbor not in parents:  # Check if neighbor is unvisited
                parents[neighbor] = current
                queue.append(neighbor)
    return parents

def get_path(parents, destination):
  path = []
  while destination is not None:
      path.append(destination)
      destination = parents.get(destination)
  return '->'.join(path[::-1])

# Sample graph
def get_sample_graph():
     return {'s': {('a', 1), ('b', 1)},
            'a': {('b', 1)},
            'b': {('c', 1)},
            'c': {('a', 1), ('d', 1)},
            'd': set()
            }
