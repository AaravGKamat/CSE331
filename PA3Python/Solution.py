import sys
from collections import deque
import time
# find a, go through all of a's edges, then add b
# then go through all outgoing edges of a and b, finding the min edge from all of those and add c


class Solution:

    def __init__(self, graph):
        self.graph = graph

    def output_edges(self):
        # creates list with every index = -1
        min_edges = [-1]*len(self.graph)
        visited = set()
        visited.add(0)
        i = 0
        min_edge = (None, None, None)
        current_node = 0
        # find min edge for node, and maintain visited dictionary
        min_edge_node = {}

        while len(visited) != len(self.graph):
            for i in range(0, len(self.graph)):
                if (i not in visited):
                    for j in visited:
                        current_node = j
                        current_weight = self.graph[current_node][i]
                        if (current_weight != -1):
                            if (min_edge[2] == None):
                                min_edge = (current_node, i, current_weight)
                            else:
                                if (current_weight < min_edge[2]):
                                    min_edge = (current_node, i,
                                                current_weight)

            if (min_edge[1] != None):
                # set parent in result
                min_edges[min_edge[1]] = min_edge[0]
                visited.add(min_edge[1])
                min_edge = (None, None, None)

            # disconected graph
            else:
                break

        return min_edges

    # def output_edges(self):
    #     # creates list with every index = -1
    #     min_edges = [-1]*len(self.graph)
    #     visited = set()
    #     visited.add(0)
    #     i = 0
    #     min_edge = (None, None, None)
    #     current_node = 0
    #     # find min edge for node, and maintain visited dictionary
    #     min_edge_node = {}

    #     while len(visited) != len(self.graph):

    #         for i in visited:
    #             current_node = i
    #             for j in range(0, len(self.graph)):
    #                 current_weight = self.graph[current_node][j]
    #                 if (j not in visited and current_weight != -1):
    #                     if (min_edge[2] == None):
    #                         min_edge = (current_node, j, current_weight)
    #                     else:
    #                         if (current_weight < min_edge[2]):
    #                             min_edge = (current_node, j, current_weight)

    #         if (min_edge[1] != None):
    #             min_edges[min_edge[1]] = min_edge[0]
    #             visited.add(min_edge[1])
    #             min_edge = (None, None, None)

    #         # disconected graph
    #         else:
    #             break

    #     return min_edges

    # def output_edges1(self):
    #     # creates list with every index = -1
    #     min_edges = [-1]*len(self.graph)
    #     edgeTo = {}
    #     visited = set()
    #     queue = deque()
    #     # go through every row, ie the edges for each node
    #     visited.add(0)
    #     queue.add(0)
    #     # traverse till queue is empty
    #     # mutable
    #     for i in visited:
    #         current = queue.popleft()
    #         min_edgeq = {}
    #         min_weight = "empty"
    #         for j in range(0, len(self.graph)):
    #             # print(j)
    #             # print(min_edgeq)
    #             # print(min_edges)
    #             # print(visited)
    #             if (j not in visited):
    #                 current_weight = self.graph[current][j]
    #                 if (current_weight != -1):
    #                     if min_weight == "empty":
    #                         min_weight = current_weight
    #                         min_edgeq[current] = j
    #                     elif current_weight < min_weight:
    #                         min_weight = current_weight
    #                         min_edgeq[current] = j
    #         if (len(min_edgeq) != 0):
    #             visited.add(min_edgeq[current])
    #             # the parent is set for the child with the edge belonging to the MST
    #             min_edges[min_edgeq[current]] = current
    #             for i in visited:
    #                 if (i not in queue):
    #                     queue.add(i)
        ########### Output the node ids of the smallest weighted path ############
        return min_edges
