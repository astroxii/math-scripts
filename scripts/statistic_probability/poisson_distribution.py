import math

# Script by astroxii @ 2022
# Have fun!


def poisson_distribution(_lambda: int, x: int) -> float:
    return ((_lambda ** x) * (math.e ** -_lambda)) / math.factorial(x)



# print("Chances of 25 cars be at a garage which's daily mean is 17 is...")
# prob = poisson_distribution(17, 25) * 100
# print(f"~ {prob:.2f}%")