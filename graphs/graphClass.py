class Graph
""" """
    def __init__(self):
        pass
        
        # implementation1:
        # 
        # 

class Node:
  # implementation1:
        #  each node is an object,
        #  each edge is a pointer.
    def __init__(self):
       self. neighbors = []
      #  O(1)
    def addNeighbors(self, neighbor_node)
        self.neighbors.append(neighbor_node)
        #  O(1)
    def getNeighbors():
        return self.neighbors
        # O(n)
    def isNeighbors(sef, node):
        return node in self.neighbors

edge_list = [
  # one directional pointers list
  (1,2),
  (1,4),
  (1,7),
  (2,3),
  (2,5),
  (3,6),
  (4,7),
  (5,6),
  (6,7)
]

# Add neighborO(1)
# check all the edges connected to 5 = O(n)

adjacency_list = {
  1: [2,4,7],
  2: [1,3,5],
  3: [2,6],
  4: [1,7],
  5: [2,6],
  6: [3,5,7],
  7: [1,4,6]
  8:
  9:
}

# addNeighbor() = O(1)

# edge_list = [
#   # two directional pointers list
#   (1,2), (2,1),
#   (1,4), (4,1),
#   (1,7), (7,1),
#   (2,3), (3,2),
#   (2,5), (5,2),
#   (3,6), (6,3),
#   (4,7), (7,4),
#   (5,6), (6,5),
#   (6,7), (7,6),
# ]

adjacency_matrix = [
  1: [0,1,0,1,0,0,1],
  2: [1,0,1,0,1,0,0],
  3: [0,1,0,0,0,1,0],
  4: [1,0,0,0,0,0,1],
  5: [0,1,0,0,0,1,0],
  6: [0,0,1,0,1,0,1],
  7: [1,0,0,1,0,1,0]
]

adjacency_matrix = {
  1: [0,1,0,1,0,0,1,0],
  2: [1,0,1,0,1,0,0,0],
  3: [0,1,0,0,0,1,0,0],
  4: [1,0,0,0,0,0,1,0],
  5: [0,1,0,0,0,1,0,0],
  6: [0,0,1,0,1,0,1,0],
  7: [1,0,0,1,0,1,0,0],
  8: [0,0,0,0,0,0,0,0]
}