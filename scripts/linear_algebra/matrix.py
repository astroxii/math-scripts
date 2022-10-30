class Matrix(list):
    def __init__(self, data = None, rolls = None, columns = None) -> None:
        self.rolls = rolls if rolls else len(data)
        self.columns = columns if columns else len(data[0])
        
        if(rolls and columns):
            for i in range(0, self.rolls):
                self.append([])
                for _ in range(0, self.columns):
                    self[i].append(0)
        elif(data):
            self.extend(data)


    def dimension(self) -> int | tuple:
        return self.rolls if self.rolls == self.columns else (self.rolls, self.columns)

    def determinant(self) -> float | int:
        assert self.rolls == self.columns, "Matrix must be square for determinant calculation."
        
        if self.dimension() == 1: return self[0][0]
        elif self.dimension() == 2: return (self[0][0]*self[1][1])-(self[0][1]*self[1][0])
        elif self.dimension() == 3:
            det = 0
            t_mat = self.copy()
            t_mat.append([t_mat[0][0], t_mat[0][1]])
            t_mat.append([t_mat[1][0], t_mat[1][1]])
            t_mat.append([t_mat[2][0], t_mat[2][1]])
            print(t_mat)
            
            for i in range(3):
                pass

            return det
    
    def multiply(m):
        pass



mat0 = Matrix(None, 2, 2) # 0 matrix
a = Matrix(data=[[2, 3, -5], [1, 0, 7], [4, -6, -2]])

print(a)
print(a.determinant())