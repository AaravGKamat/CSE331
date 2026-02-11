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

    def generate_matches2(self):
        # list of all possible matchings
        result = []
        matching_list = []
        match_list = []
        men_list = list(self.men.keys())
        print(self.men[men_list[0]][0])
        taken = []
        match_list = []
        for j in range(0, len(men_list)):
            for i in range(0, 3):
                anchor_match = Marriage(men_list[j], self.men[men_list[j]][i])
                match_list.append(anchor_match)
                taken.append(self.men[men_list[j]][i])
                for man in self.men:

                    if (man != anchor_match.man()):
                        for woman in self.men[man]:
                            if woman not in taken:
                                match = Marriage(man, woman)
                                taken.append(woman)
                                match_list.append(match)
                                break

                    else:
                        continue

                matching_list.append(match_list)
                match_list = []
                taken = []

            print(matching_list)
            result.append(matching_list)
            matching_list = []
        print(result)
        return result

    def output_stable_matchings(self):
        result = self.generate_matches2()
        for matching_list in result:
            for list in matching_list:
                for match in list:
                    i = 1

        """
        This method both computes and returns the stable matchings
        :return: the list of stable matchings
        """
        return self.stable_matchings

    # make all possible matchings
