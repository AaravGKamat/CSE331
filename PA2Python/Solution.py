from collections import deque
import numpy as np

# CITE TB BFS


class Solution:

    def __init__(self, start_node, graph):
        self.start_node = start_node
        self.graph = graph

    def output_distances(self):
        # maps node to its level/distance from start node
        # print(self.graph)
        # list of visited nodes
        visited = []
        # the level if the node, ie its distance from the start node in terms of edges
        level = 0
        # a dictionary from level:list of nodes, keeping track of the number of nodes in each level
        level_nodes = {}
        level_nodes[level] = [self.start_node]
        # the final list, where the index denotes the node, and the value at the index denotes its distance from the start node
        distance = np.empty(len(self.graph))
        distance[self.start_node] = level
        visited.append(self.start_node)
        # the loop continues until all nodes are explored, in which case the list of nodes at that level will be empty
        while len(level_nodes[level]) != 0:
            next_level = []
            # explore all edges incident to a node
            for node in level_nodes[level]:
                for neighbor in self.graph.get(node):
                    if neighbor not in visited:
                        visited.append(neighbor)
                        next_level.append(neighbor)
                        distance[neighbor] = level + 1

            level += 1
            level_nodes[level] = next_level

        # convert numpy list to python list
        distance = distance.astype(int).tolist()
        # all unvisited nodes are not part of the BFS spanning tree
        for node in self.graph:
            if node not in visited:
                distance[node] = -1
        # print(result)

        # map every level to all the nodes it has, make sure no duplicates

        """
        :return: the list of minimum distances from each node to the start node
        """
        return distance
