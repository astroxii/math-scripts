from math import sqrt

# Script by astroxii @ 2022
# Have fun!


class Array(list):
    def __init__(self, items: list):
        self.extend(items)
        self.sort()

    def mean(self) -> float | int:
        return sum(self) / len(self)

    def median(self) -> float | int:
        return self[(len(self)-1)//2] if len(self) % 2 == 1 else ((self[(len(self))//2]+self[(len(self))//2])/2)

    def mode(self) -> list | float | int | None:
        modes = []

        for i in range(len(self)):
            if i+1 < len(self):
                if self[i] == self[i+1] and self[i] not in modes:
                    modes.append(self[i])

        return modes if len(modes) > 1 else modes[0] if len(modes) == 1 else None

    def deviation(self) -> list:
        d = []

        for i in self:
            d.append(abs(self.mean()-i))

        return d

    def variance(self) -> float | int:
        sdv = []

        for d in self.deviation():
            sdv.append(pow(d, 2))

        v = sum(sdv) / len(self)

        return v

    def std_deviation(self) -> float | int:
        return sqrt(self.variance())


myArray = Array(items=[21, 4, 22, 12, 19, 18, 15, 7, 21, 9, 7])
print(myArray)
print(myArray.median())
print(myArray.mode())
print(myArray.std_deviation())
