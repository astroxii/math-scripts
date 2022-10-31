from math import sqrt

# Script by astroxii @ 2022
# Have fun!


class Array(list):
    def __init__(self, items: list):
        super().__init__()
        self.extend(items)

    def mean(self) -> float | int:
        return sum(self) / len(self)
    
    def harmonic_mean(self) -> float | int:
        return len(self)/(sum([1/x for x in self]))

    def median(self) -> float | int:
        return sorted(self)[(len(self)-1)//2] if len(self) % 2 == 1 else ((sorted(self)[(len(self))//2]+sorted(self)[(len(self))//2])/2)

    def mode(self) -> dict | None:
        modes = {}

        for i in range(len(self)):
            if i+1 < len(self):
                if sorted(self)[i] == sorted(self)[i+1] and sorted(self)[i] not in modes:
                    modes[sorted(self)[i]] = 1
                elif sorted(self)[i] in modes:
                    modes[sorted(self)[i]] += 1

        return modes if modes else None

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

    def unique(self) -> list:
        u = []

        for i in self:
            if i not in u:
                u.append(i)
        
        return u


myArray = Array(items=[15, 28, 32, 17, 19, 13, 11, 26, 23, 29, 14, 16, 18, 22, 24, 25, 27, 30, 29, 15])
# print(myArray)
# print(myArray.mean())
# print(myArray.harmonic_mean())
# print(myArray.median())
print(myArray.mode())
# print(myArray.std_deviation())
# print(myArray.unique())
