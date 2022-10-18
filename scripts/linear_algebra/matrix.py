class Matrix(list):
    def __init__(self, rolls = 1, columns = 1) -> None:
        self.rolls = rolls
        self.columns = columns

        for i in range(0, rolls):
            self.append([])
            for j in range(0, columns):
                self[i].append(j+2+i)

    def dimension(self) -> int | tuple:
        return self.rolls if self.rolls == self.columns else (self.rolls, self.columns)

    def determinant(self) -> float | int:
        assert self.rolls == self.columns, "Matrix must be square for determinant calculation."
        
        if self.dimension() == 1: return self[0][0]
        elif self.dimension() == 2: return (self[0][0]*self[1][1])-(self[0][1]*self[1][0])
        elif self.dimension() == 3:
            pass



mat = Matrix(2, 2)

print(mat)
print(mat.determinant())