import math


class QuadraticFunction:
    def __init__(self, a = 1, b = 0, c = 0) -> None:
        self.a = a
        self.b = b
        self.c = c

    def get_delta(self) -> float | int:
        return math.pow(self.b, 2) - (4*self.a*self.c)

    def get_roots(self) -> tuple:
        x1 = x2 = 0
        delta = self.get_delta()

        x1 = ((-self.b + math.sqrt(delta))/2*self.a if delta >= 0 else None)
        x2 = ((-self.b - math.sqrt(delta))/2*self.a if delta >= 0 else None)

        return (x1, x2)

    def get_vertex(self) -> tuple:
        x = y = 0
        delta = self.get_delta()

        x = -self.b/2*self.a
        y = -delta/4*self.a

        return (x, y)

    def __str__(self) -> str:
        return f"{self.a}^2 {self.b:+} {self.c:+}"


qf = QuadraticFunction(5, 20, 10)
print(qf.get_delta())
print(qf.get_roots())
print(qf.get_vertex())
print(qf)