import math


class Vector:
    def __init__(self, x: int | float = None, y: int | float = None, z: int | float = None) -> None:
        assert x != None and y != None, "Vector must have at least two dimensions."
        assert abs(x) + abs(y) > 0, "Vector is null."

        self.x = x
        self.y = y
        self.z = z
        self.dimension = 2 if self.z == None else 3


    def modulus(self) -> int | float:
        return math.sqrt((self.x ** 2) + (self.y ** 2) + (self.z ** 2 if self.z != None else 0))


    def dot_product(self, vector = None) -> int | float:
        assert isinstance(vector, Vector), "Must specify a Vector for scalar calculation."
        assert self.dimension == vector.dimension, "Vectors dimensions must be equal."

        return (self.x * vector.x) + (self.y * vector.y) + (self.z * vector.z if self.z != None and vector.z != None else 0)


    def angle_to(self, vector = None, unit = "deg") -> int | float:
        assert isinstance(vector, Vector), "Must specify a Vector for angle calculation."
        assert self.dimension == vector.dimension, "Vectors dimensions must be equal."
        assert self is not vector, "Calculation of angle to same vector."

        return math.acos(self.dot_product(vector) / (self.modulus() * vector.modulus())) * ((180 / math.pi) if unit == "deg" else 1)


    def __str__(self) -> str:
        return f"Vector {str(self.dimension)}D <X={self.x}, Y={self.y}{f', Z={self.z}>' if self.z != None else '>'}"



v1 = Vector(1, 2, 2)
v2 = Vector(-1, 0, 2)
print(v1)
print(v1.dot_product(v1))
print(v1.angle_to(v2))