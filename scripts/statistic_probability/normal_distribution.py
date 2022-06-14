import math

# Script by astroxii @ 2022
# Have fun!


def normal_distribution(sigma: float | int, mu: float | int, x: float | int) -> float:
    return ((1/(sigma*math.sqrt(2*math.pi)))*(math.e ** (-0.5*((x-mu/sigma)**2))))
