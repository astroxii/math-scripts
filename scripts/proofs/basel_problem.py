from math import pi

# What's the result of an infinite sum of the inverse squares of numbers x, where x > 0
# Euler's solution: pi^2/6

r = sum([1/(x**2) for x in range(1, 10000)])

print(r, (pi**2)/6)