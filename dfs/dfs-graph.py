class DFSGraph:
  def __init__(self):
      self.graph = {}
  def add_edge(self, u, v):
    if u not in self.graph:
      self.graph[u] = []
    self.graph[u].append(v)

  def dfs(self, start, visited = None):
    if visited is None:
      visited = set()
    visited.add(start)
    print(start, end = ' ')
    for next in self.graph.get(start, []):
      if next not in visited:
        self.dfs(next, visited)
        


my_graph = DFSGraph()
my_graph.add_edge(1, 2)
my_graph.add_edge(1, 3)
my_graph.add_edge(2, 4)
my_graph.add_edge(2, 5)
my_graph.add_edge(3, 6)
my_graph.add_edge(3, 7)

# Perform DFS starting from node 1
print("DFS traversal starting from node 1:")
my_graph.dfs(1)
