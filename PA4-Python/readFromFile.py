def readFromFile(inputFile):

	points = []

	with open(inputFile, 'r') as file:

		numberOfPoints = int(file.readline())
		
		for i in range(0, numberOfPoints):
			xyCoords = file.readline().split()
			points.append((float(xyCoords[0]), float(xyCoords[1])))

	return points
	