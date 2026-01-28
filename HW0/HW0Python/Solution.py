class Solution:

    def __init__(self, in_vector):
        """
        The constructor exists only to initialize variables.
        You do not need to change it.
        :param in_vector: The vector given from the file, as a list
        """
        self.in_vector = in_vector

    # def output_vector(self):
    #     """
    #     This method must be filled in by you. You may add
    #     other methods and subclasses as you see fit,
    #     but they must remain within the Solution class.
    #     :return: a correct output vector, as a Python list
    #     """

    #     result = []
    #     # number of elements in the vector
    #     length = len(self.in_vector)

    #     # sum of all elements, so the first entry in the resulting vector
    #     sum = 0
    #     for i in range(0, length):
    #         sum += self.in_vector[i]

    #     result.append(sum)
    #     for i in range(1, length):
    #         num = result[0]
    #         while i > 0:
    #             num = num - self.in_vector[i-1]
    #             i -= 1
    #         result.append(num)

    #     return result

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

        sub = self.in_vector[0]
        for i in range(1, length):
            num = result[0] - sub
            sub += self.in_vector[i]

            result.append(num)

        return result


def column_create(ones, rows):
    result = []
    for i in range(0, rows):
        if (ones > 0):
            result.append(1)
        else:
            result.append(0)
        ones = ones-1
    return result


def row_create(zeroes, rows):
    result = []
    for i in range(0, rows):
        if (zeroes > 0):
            result.append(0)
        else:
            result.append(1)
        zeroes = zeroes-1
    return result
