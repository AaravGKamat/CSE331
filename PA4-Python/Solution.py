from operator import itemgetter, attrgetter
import math
import heapq


class Solution:
    def __init__(self, points):
        self.points = points

    class PointElement:
        # I negatve because maxheap is not implemented in Autograder's version of Python
        def __init__(self, x, y):
            self.id = id
            self.x = x
            self.y = y

        # Overloading operator for minheap
        def __lt__(self, other):
            if (self.y != other.y):
                return self.y < other.y
            else:
                return self.x < other.x

    def findClosestPairHelper(self, sorted_point_list_x, sorted_point_list_y):
        min_length = 3
        if (len(sorted_point_list_x) <= min_length):
            return self.bruteForce(sorted_point_list_x)

        mid = math.floor(len(sorted_point_list_x)/2)
        midpoint = sorted_point_list_x[mid]

        Qx = sorted_point_list_x[:mid]
        Rx = sorted_point_list_x[mid:]

        Qy = []
        Ry = []

        for point in sorted_point_list_y:
            if (point.x <= midpoint.x):
                Qy.append(point)
            else:
                Ry.append(point)

        dist1 = self.findClosestPairHelper(Qx, Qy)
        dist2 = self.findClosestPairHelper(Rx, Ry)
        minof2 = min(dist1, dist2)

        strip = []
        for point in sorted_point_list_y:
            if (abs(point.x - midpoint.x) < minof2):
                strip.append(point)

        return min(minof2, self.checkStrip(strip, minof2))

    def checkStrip(self, strip, mindist):
        mindist = mindist
        for i in range(0, len(strip)):
            point1 = strip[i]

            for j in range(i+1, len(strip)):
                point2 = strip[j]

                if (point2.y - point1.y >= mindist):
                    break

                distance = math.dist([point1.x, point1.y], [
                                     point2.x, point2.y])
                if (distance < mindist):
                    mindist = distance
        return mindist

    def bruteForce(self, pointlist):
        min = 0
        for i in range(0, len(pointlist)):
            for j in range(i+1, len(pointlist)):
                if (pointlist[i] != pointlist[j]):
                    distance = math.dist([pointlist[i].x, pointlist[i].y],
                                         [pointlist[j].x, pointlist[j].y])
                    if (min == 0 or distance < min):
                        min = distance
        return min

    def findClosestPair(self):
        # create a new list containing points as PointElement objects
        for i in range(0, len(self.points)):
            self.points[i] = self.PointElement(
                self.points[i][0], self.points[i][1])

        # sort the points based on x coordinates and break clashes based on y coordinates
        sort_by_x = (sorted(self.points, key=attrgetter("x", "y")))
        sort_by_y = (sorted(self.points, key=attrgetter("y", "x")))
        # for pt in sort_by_x:
        #     print("Point = (%d,%d)" % (pt.x, pt.y))

        return self.findClosestPairHelper(sort_by_x, sort_by_y)
