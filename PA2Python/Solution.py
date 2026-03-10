from collections import deque
import numpy as np


class Solution:

    def __init__(self, start_node, graph):
        self.start_node = start_node
        self.graph = graph

    def output_distances(self):
        # maps node to its level/distance from start node
        visited = []
        queue = deque()
        queue.append(self.start_node)
        level = 0
        leveler = {}
        leveler[level] = [self.start_node]
        while len(leveler[level]) != 0:
            next = []
            for node in leveler[level]:
                for edge in self.graph.get(node):
                    if edge not in visited:
                        visited.append(edge)
                        next.append(edge)

            level += 1
            leveler[level] = next

        result = np.empty(len(self.graph))
        for distance in leveler.keys():
            nodes = leveler[distance]
            for node in nodes:
                result[node] = distance

        result = result.astype(int).tolist()

        # map every level to all the nodes it has, make sure no duplicates

        """
        :return: the list of minimum distances from each node to the start node
        """
        return result
