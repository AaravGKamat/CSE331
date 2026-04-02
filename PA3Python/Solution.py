import sys
from collections import deque

# find a, go through all of a's edges, then add b
# then go through all outgoing edges of a and b, finding the min edge from all of those and add c


class Solution:

    def __init__(self, graph):
        self.graph = graph

    def output_edges(self):
        # creates list with every index = -1
        min_edges = [-1]*len(self.graph)
        edgeTo = {}
        visited = []
        queue = deque()
        # go through every row, ie the edges for each node
        visited.append(0)
        queue.append(0)
        # traverse till queue is empty
        # mutable
        for i in visited:
            current = queue.popleft()
            min_edgeq = {}
            min_weight = "empty"
            for j in range(0, len(self.graph)):
                # print(j)
                # print(min_edgeq)
                # print(min_edges)
                # print(visited)
                if (j not in visited):
                    current_weight = self.graph[current][j]
                    if (current_weight != -1):
                        if min_weight == "empty":
                            min_weight = current_weight
                            min_edgeq[current] = j
                        elif current_weight < min_weight:
                            min_weight = current_weight
                            min_edgeq[current] = j
            if (len(min_edgeq) != 0):
                visited.append(min_edgeq[current])
                # the parent is set for the child with the edge belonging to the MST
                min_edges[min_edgeq[current]] = current
                for i in visited:
                    if (i not in queue):
                        queue.append(i)
        ########### Output the node ids of the smallest weighted path ############
        return min_edges
