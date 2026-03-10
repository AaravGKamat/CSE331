from collections import deque


class Solution:

    def __init__(self, start_node, graph):
        self.start_node = start_node
        self.graph = graph

    def output_distances(self):
        # maps node to its level/distance from start node
        visited = {}
        queue = deque()
        # edgeTo = []
        edgeTo = {}
        queue.append(self.start_node)
        level = 0
        leveler = {}
        visited[self.start_node] = level
        # map every level to all the nodes it has, make sure no duplicates
        while (len(queue) != 0):

            current = queue.popleft()

            level += 1
            for neighbor in self.graph.get(current):

                if neighbor not in visited:
                    visited[neighbor] = level
                    edgeTo[neighbor] = current
                    # edgeTo.append((neighbor, current))
                    queue.append(neighbor)

            for i in queue:
                if i not in leveler:
                    leveler[i] = level

        distances = []
        for key in sorted(visited.keys()):

            distances.append(visited[key])

        print("\n")
        print(leveler)

        # for key in edgeTo:
        #     i = 0
        #     if key == self.start_node:
        #         distances[self.start_node] = 0
        #     else:
        #         current = key
        #         while (key != self.start_node):
        #             current = edgeTo[key]
        #             i += 1
        #     distances[key] = 1

        """
        :return: the list of minimum distances from each node to the start node
        """
        return distances
