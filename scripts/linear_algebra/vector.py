import math


class Vector:
    def __init__(self, x: int | float = None, y: int | float = None, z: int | float = None) -> None:
        assert x != None and y != None, "Vector must have at least two dimensions."

        self.x = x
        self.y = y
        self.z = z
        self.dimension = 2 if self.z == None else 3

    def modulus(self) -> int | float:
        return math.sqrt((self.x ** 2) + (self.y ** 2) + (self.z ** 2 if self.z != None else 0))

    def __str__(self) -> str:
        return f"Vector {str(self.dimension)}D (X = {self.x}, Y = {self.y}{f', Z = {self.z})' if self.z != None else ')'}"


v1 = Vector(3, 4)
print(v1)
print(v1.modulus())