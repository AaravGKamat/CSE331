from Solution import *
from readFromFile import *
import sys

def main():

	if (len(sys.argv) < 2):
		print("Please provide the input filepath as the argument")
		sys.exit()

	input_file = sys.argv[1]

	input = readFromFile(input_file)

	#Get answer
	solution = Solution(input)
	print(solution.findClosestPair())

if __name__ == '__main__':
	main()
