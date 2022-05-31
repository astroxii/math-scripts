from math import sqrt

# Script by astroxii @ 2022
# Have fun!


class Array(list):
    def __init__(self, items: list):
        self.extend(items)

    def mean(self) -> float:
        return sum(self) / len(self)

    def deviation(self) -> list:
        d = []

        for i in self:
            d.append(abs(self.mean()-i))

        return d

    def variance(self) -> float:
        sdv = []

        for d in self.deviation():
            sdv.append(pow(d, 2))

        v = sum(sdv) / len(self)

        return v

    def std_deviation(self) -> float:
        return sqrt(self.variance())


myArray = Array(items=[21, 4, 22, 15, 19, 18, 15, 7])
print(myArray)
