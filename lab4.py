#Exercitiul 1
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None  # Return None if the stack is empty

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None  # Return None if the stack is empty

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    

    #Exercitiul2   
     
    class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None  # Return None if the stack is empty

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None  # Return None if the stack is empty

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


#Exercitiul 3
class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def get(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.data[row][col]
        else:
            return None  # Return None for out-of-bounds access

    def set(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.data[row][col] = value
        else:
            print("Invalid row or column index")

    def transpose(self):
        transposed_matrix = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                transposed_matrix.set(j, i, self.get(i, j))
        return transposed_matrix

    def multiply(self, other):
        if self.cols != other.rows:
            print("Invalid dimensions for matrix multiplication")
            return None

        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result

    def apply_function(self, func):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = func(self.data[i][j])

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])
