import sys
from Solution import Solution

def main():
    if (len(sys.argv) < 2):
        print("Please provide the input filepath as the argument")
        sys.exit()

    input_file = sys.argv[1]
    graph = []
    node = 0

    # Reading and parsing the file
    with open(input_file, 'r') as file:
        for line in file:
            adjList = [int(neighbor) for neighbor in line.split()]
            graph.append(adjList)
            node += 1

    # Get the path
    path = Solution(graph).output_edges();
    #print('Your Solution:')
    #print('=========================================================')
    print(path)
    #print('=========================================================')

if __name__ == '__main__':
    main()
