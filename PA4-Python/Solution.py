from operator import itemgetter, attrgetter


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
            return 0

    def findClosestPairHelper(self, sorted_point_list):
        return 0

    def findClosestPair(self):
        # create a new list containing points as PointElement objects
        new_list = []
        for point in self.points:
            new_point = self.PointElement(point[0], point[1])
            new_list.append(new_point)
        # sort the points based on x coordinates and break clashes based on y coordinates
        sort_by_x = (sorted(new_list, key=attrgetter("x", "y")))
        for pt in sort_by_x:
            print("Point = (%d,%d)" % (pt.x, pt.y))

        result = self.findClosestPairHelper(sort_by_x)
