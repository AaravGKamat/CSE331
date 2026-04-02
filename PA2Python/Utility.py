import re
from Graph import Graph

class Utility:

    def read_file(self, input_file):
        start_node = 0
        node = 0
        graph = {}
                    
        #Reading and parsing the file
        with open(input_file, 'r') as file:
            start_node = int(file.readline())
            for line in file:
                adjList = [int(neighbor) for neighbor in line.split()]
                graph[node] = adjList
                node += 1

        return Graph(start_node, graph)