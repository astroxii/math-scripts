import math

# Script by astroxii @ 2022
# Have fun!


class GeometricProgression:
    def __init__(self):
        pass

    @staticmethod
    def sequence_a1(q: float, n: int, a1: float) -> list:
        seq = [a1]

        for i in range(1, n):
            seq.append(seq[i-1]*q)

        return seq

    @staticmethod
    def sequence(q: float, n: int) -> list:
        seq = [q]

        for i in range(1, n):
            seq.append(seq[i-1]*q)

        return seq

    @staticmethod
    def get_sum(seq: list) -> float:
        return (seq[0]*((GeometricProgression.get_diff(seq)**len(seq)) - 1))/(GeometricProgression.get_diff(seq) - 1)

    @staticmethod
    def get_mid_term(seq: list) -> float:
        return math.sqrt(seq[0]*seq[len(seq)-1])

    @staticmethod
    def get_diff(seq: list) -> float:
        return seq[1] / seq[0]

    @staticmethod
    def get_term_a1(q: float, n: int, a1: float) -> float:
        return a1*(q**(n-1))

    @staticmethod
    def get_term_seq(seq: list, n: int) -> float:
        return seq[0]*(GeometricProgression.get_diff(seq)**(n-1)) # But it will be same as seq[n-1], if n-1 index exists


# myGP = GeometricProgression.sequence(2, 5)
# print(myGP)
# print(GeometricProgression.get_diff(myGP))
# print(GeometricProgression.get_term_a1(2, 4, 2))
# print(GeometricProgression.get_term_seq(myGP, 4))
# print(GeometricProgression.get_sum(myGP))
# print(GeometricProgression.get_mid_term(myGP))
