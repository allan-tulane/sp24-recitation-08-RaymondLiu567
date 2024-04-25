# CMPS 2200 Recitation 08

## Answers

**Name:**_______Raymond Liu__________________


Place all written answers from `recitation-08.md` here for easier grading.



- **1b)**
Work Complexity (W):
The work complexity for Dijkstra's algorithm, denoted as W(E, V), is the sum of the work done over all vertices and the work done over all edges. Specifically:

The work over all vertices, W(V), typically involves initializing the algorithm, which is O(V) since each vertex is processed for setup.
The work over all edges, W(E * logV), takes into account the priority queue operations for each edge, such as adding and updating nodes in the queue, which is O(logV) for a binary heap.
The total work complexity, W(E, V), is therefore the sum of these two terms:

W(E, V) = W(V) + W(E * logV) = O(V + ElogV)

Span Complexity (S):
The span complexity, denoted as S(E, V), represents the longest path of dependencies in the execution of the algorithm. In Dijkstra's algorithm, the span is governed by the sequential heap operations:

Because the priority queue is central to the algorithm and its operations are sequential (not parallelizable), the span is not O(E) as might be mistakenly assumed for an edge-dominant operation. Instead, for each of the V vertices, a series of O(logV) operations may be needed, such as extracting the minimum-distance node.
The correct span complexity should thus be represented as:

S(E, V) = O(VlogV)

- **2b)**
def get_path(parents, destination):
  path = []
  while destination is not None:
      path.append(destination)
      destination = parents.get(destination)
  return '->'.join(path[::-1])