from operator import itemgetter, attrgetter
import math
import heapq


class Solution:
    def __init__(self, points):
        self.points = points

    class PointElement:
        def __init__(self, x, y):
            self.id = id
            self.x = x
            self.y = y

        # Overloading operator
        def __lt__(self, other):
            if (self.y != other.y):
                return self.y < other.y
            else:
                return self.x < other.x

    def findClosestPairHelper(self, sorted_point_list):
        min_length = 3
        if len(sorted_point_list) <= min_length:
            current_min = 0
            # brute force calculation of minimum distance
            for i in range(0, len(sorted_point_list)):
                for j in range(0, len(sorted_point_list)):
                    if (sorted_point_list[i] != sorted_point_list[j]):
                        distance = (math.dist([sorted_point_list[i].x, sorted_point_list[i].y], [
                            sorted_point_list[j].x, sorted_point_list[j].y]))
                        if (current_min == 0 or distance < current_min):
                            current_min = distance
            return current_min

        else:
            left_d = self.findClosestPairHelper(
                sorted_point_list[:math.floor(len(sorted_point_list)/2)])
            right_d = self.findClosestPairHelper(
                sorted_point_list[math.floor(len(sorted_point_list)/2):])
            min_dist = min(left_d, right_d)
            # center of dividing line
            midpoint = math.floor(len(sorted_point_list)/2)
            range_x = [sorted_point_list[midpoint].x - min_dist,
                       sorted_point_list[midpoint].x + min_dist]
            strip_points = []
            length = 0
            for point in sorted_point_list:
                if point.x >= range_x[0] and point.x <= range_x[1]:
                    strip_points.append(point)
                    length += 1
            strip_points = sorted(strip_points, key=attrgetter("y", "x"))
            # brute force compare each point to the next 7 points
            true_min = min_dist
            done = set()

            # leng = 15
            # if (length < 15):
            #     leng = length
            # for i in range(0, leng):
            #     for j in range(0, leng):
            #         if (i+j < leng):
            #             point1 = strip_points[i]
            #             point2 = strip_points[i+j]
            #             if (point1 != point2 and abs(point1.y - point2.y) <= min_dist):
            #                 distance = (math.dist([point1.x, point1.y], [
            #                     point2.x, point2.y]))
            #                 if (distance < true_min):
            #                     true_min = distance
            #                 done.add((point1, point2))

            for point1 in strip_points:
                for point2 in strip_points:
                    if (abs(point1.y - point2.y) >= min_dist):
                        break
                    if (point1 != point2):
                        distance = (math.dist([point1.x, point1.y], [
                            point2.x, point2.y]))
                        if (true_min == 0 or distance < true_min):
                            true_min = distance
                        done.add((point1, point2))

            if (true_min == 0):
                true_min = min_dist
            return true_min

    def findClosestPair(self):
        # create a new list containing points as PointElement objects

        for i in range(0, len(self.points)):
            self.points[i] = self.PointElement(
                self.points[i][0], self.points[i][1])

        # sort the points based on x coordinates and break clashes based on y coordinates
        sort_by_x = (sorted(self.points, key=attrgetter("x", "y")))
        # for pt in sort_by_x:
        #     print("Point = (%d,%d)" % (pt.x, pt.y))

        return self.findClosestPairHelper(sort_by_x)
