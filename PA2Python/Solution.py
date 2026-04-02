from collections import deque
import numpy as np

# CITE TB BFS


class Solution:

    def __init__(self, start_node, graph):
        self.start_node = start_node
        self.graph = graph

    def output_distances(self):
        # # maps node to its level/distance from start node
        # # print(self.graph)
        # # list of visited nodes
        # visited = set()
        # # the level if the node, ie its distance from the start node in terms of edges
        # level = 0
        # # a dictionary from level:list of nodes, keeping track of the number of nodes in each level
        # level_nodes = {}
        # level_nodes[level] = [self.start_node]
        # # the final list, where the index denotes the node, and the value at the index denotes its distance from the start node
        # distance = np.empty(len(self.graph))
        # distance[self.start_node] = level
        # visited.add(self.start_node)
        # # the loop continues until all nodes are explored, in which case the list of nodes at that level will be empty
        # while len(level_nodes[level]) != 0:
        #     next_level = []
        #     # explore all edges incident to a node
        #     for node in level_nodes[level]:
        #         for neighbor in self.graph.get(node):
        #             if neighbor not in visited:
        #                 visited.add(neighbor)
        #                 next_level.append(neighbor)
        #                 distance[neighbor] = level + 1

        #     level += 1
        #     level_nodes[level] = next_level

        # # convert numpy list to python list
        # distance = distance.astype(int).tolist()
        # # all unvisited nodes are not part of the BFS spanning tree
        # for node in self.graph:
        #     if node not in visited:
        #         distance[node] = -1
        # # print(result)

        # # map every level to all the nodes it has, make sure no duplicates

        # """
        # :return: the list of minimum distances from each node to the start node
        # """
        # return distance
        distances = self.distance_BFS()
        return distances

    def distance_BFS(self):

        # maps node to its level/distance from start node
        visited = set()
        # the level if the node, ie its distance from the start node in terms of edges
        level = 0
        # a dictionary from node:its level, ie distance from start node
        level_nodes = {}
        level_nodes[self.start_node] = level
        # the final list, where the index denotes the node, and the value at the index denotes its distance from the start node
        distance = np.empty(len(self.graph))
        distance[self.start_node] = level
        visited.add(self.start_node)

        queue = deque()
        queue.append(self.start_node)

        while (queue):
            # print(len(queue))

            current = queue.popleft()
            if (len(queue) == 0 and current == -1):
                break
            if current not in level_nodes and current != -1:
                level_nodes[current] = level+1

            # print(queue)
            if (current == -1):
                queue.append(-1)
                level += 1

            # regular BFS with a minor change:
            # start node is level 0, its neighbors form level 1; we enqueue -1 to indicate end of a level
            # every time -1 is encountered, that is the end of the level, and we enqueue it again to signal the next level

            else:
                for neighbor in self.graph.get(current):

                    if (neighbor not in visited):
                        visited.add(neighbor)

                        queue.append(neighbor)

                if current == self.start_node:
                    queue.append(-1)

        # go through the sorted list of nodes and assign their indices in the final list to their level
        for key in sorted(level_nodes.keys()):
            distance[key] = level_nodes[key]

        # every node not part of the spanning tree has a distance of -1 from the start
        for node in self.graph:
            if node not in visited:
                distance[node] = -1

        return (distance.astype(int).tolist())
