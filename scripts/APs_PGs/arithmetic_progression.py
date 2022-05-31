# Script by astroxii @ 2022
# Have fun!

class ArithmeticProgression:
    def __init__(self):
        pass

    @staticmethod
    def sequence_a1(d: float, n: int, a1: float) -> list:
        seq = [a1]

        for i in range(1, n):
            seq.append(seq[i-1]+d)

        return seq

    @staticmethod
    def sequence(d: float, n: int) -> list:
        seq = [d]

        for i in range(1, n):
            seq.append(seq[i-1]+d)

        return seq

    @staticmethod
    def get_sum(seq: list) -> float:
        return ((seq[0]+seq[len(seq)-1])*len(seq))/2

    @staticmethod
    def get_mid_term(seq: list) -> float:
        return (seq[0]+seq[len(seq)-1])/2

    @staticmethod
    def get_diff(seq: list) -> float:
        return (seq[len(seq)-1] - seq[0]) / (len(seq)-1)

    @staticmethod
    def get_term_a1(d: float, n: int, a1: float) -> float:
        return a1 + (n - 1) * d

    @staticmethod
    def get_term_seq(seq: list, n: int) -> float:
        return seq[0] + (n - 1) * ArithmeticProgression.get_diff(seq)


myAP = ArithmeticProgression.sequence(2.5, 5)
print(myAP)
print(ArithmeticProgression.get_diff(myAP))
print(ArithmeticProgression.get_term_a1(2.5, 3, 2.5))
print(ArithmeticProgression.get_term_seq(myAP, 2))
print(ArithmeticProgression.get_sum(myAP))
print(ArithmeticProgression.get_mid_term(myAP))
