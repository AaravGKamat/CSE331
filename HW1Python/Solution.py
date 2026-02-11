from Marriage import Marriage
from itertools import permutations


class Solution:

    def __init__(self, number, women, men):
        """
        The constructor exists only to initialize variables. You do not need to change it.
        :param number: The number of members
        :param men: The preference list of men, as a dictionary.
        :param women: The preference list of the women, as a dictionary.
        """
        self.num = number
        self.men = men
        self.women = women
        self.count = 0
        self.stable_matchings = []

    def generate_matches(self):
        # list of all possible matchings
        matching_list = {}
        match_list = []
        first = True
        i = 0
        for man in self.men:
            for woman in self.men[man]:
                if (first == True):
                    new_match = Marriage(1, 1)
                    # initialize each match

                    new_match.set_man(man)
                    new_match.set_woman(woman)
                    match_list.append(new_match)
                    matching_list[i] = match_list

                    i += 1
            first = False
            print(matching_list)

    def output_stable_matchings(self):
        self.generate_matches()

        """
        This method both computes and returns the stable matchings
        :return: the list of stable matchings
        """
        return self.stable_matchings

    # make all possible matchings
