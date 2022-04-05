class StringClass:

    def __init__(self, S):
        self.S = S

    def return_length(self):
        return len(self.S)

    def convertstring_into_list(self):
        return [char for char in self.S]


class PairsPossible(StringClass):

    def __init__(self, S2):
        self. S2=S2
        StringClass.__init__(self,S="PAVAN")

    def print_possible_pairs(self):
        res = [(a, b) for idx, a in enumerate(self.S2) for b in self.S2[idx + 1:]]
        print(str(res))


class SCE(PairsPossible):
    all = []

    def __init__(self):

        PairsPossible.__init__(self, S2="DHARANI")

    def print_common_element(self):

        print(self.S2)
        print(self.S)

        for i in self.S:
            for j in self.S2:
                if i == j:
                    SCE.all.append(i)

        print(SCE.all)

















search = SCE()
search.print_common_element()
