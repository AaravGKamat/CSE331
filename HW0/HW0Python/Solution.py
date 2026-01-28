class Solution:

    def __init__(self, in_vector):
        """
        The constructor exists only to initialize variables.
        You do not need to change it.
        :param in_vector: The vector given from the file, as a list
        """
        self.in_vector = in_vector

    def output_vector(self):
        """
        This method must be filled in by you. You may add
        other methods and subclasses as you see fit,
        but they must remain within the Solution class.
        :return: a correct output vector, as a Python list
        """

        result = []
        # number of elements in the vector
        length = len(self.in_vector)

        # sum of all elements, so the first entry in the resulting vector
        sum = 0
        for i in range(0, length):
            sum += self.in_vector[i]

        result.append(sum)
        for i in range(1, length):
            num = result[0]
            while i > 0:
                num = num - self.in_vector[i-1]
                i -= 1
            result.append(num)

        return result
