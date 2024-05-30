class SparseMatrix:
    def __init__(self, file_path=None, rows=None, columns=None):
        if file_path:
            self.load_from_txt(file_path)
        elif rows and columns:
            self.rows = rows
            self.columns = columns
            self.matrix = {}

    def load_from_txt(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        try:
            self.rows = int(lines[0].split('=')[1])
            self.columns = int(lines[1].split('=')[1])
            self.matrix = {}

            for line in lines[2:]:
                row, col, value = map(int, line.strip().strip('()').split(','))
                self.set_item(row, col, value)
        except Exception as e:
            raise ValueError("Input file has wrong format") from e

    def get_item(self, currRow, currCol):
        return self.matrix.get((currRow, currCol), 0)

    def set_item(self, currRow, currCol, value):
        if value != 0:
            self.matrix[(currRow, currCol)] = value
        elif (currRow, currCol) in self.matrix:
            del self.matrix[(currRow, currCol)]

    def matrix_add(self, otherMatrix):
        result = SparseMatrix(rows=self.rows, columns=self.columns)

        for key in set(self.matrix.keys()).union(otherMatrix.matrix.keys()):
            row, col = key
            value = self.get_item(row, col) + otherMatrix.get_item(row, col)
            result.set_item(row, col, value)

        return result

    def matrix_subtract(self, otherMatrix):
        result = SparseMatrix(rows=self.rows, columns=self.columns)

        for key in set(self.matrix.keys()).union(otherMatrix.matrix.keys()):
            row, col = key
            value = self.get_item(row, col) - otherMatrix.get_item(row, col)
            result.set_item(row, col, value)

        return result

    def matrix_multiply(self, otherMatrix):
        if self.columns != otherMatrix.rows:
            raise ValueError("Number of columns of first matrix must be equal to number of rows of second matrix")

        result = SparseMatrix(rows=self.rows, columns=otherMatrix.columns)

        for i in range(self.rows):
            for j in range(otherMatrix.columns):
                value = sum(self.get_item(i, k) * otherMatrix.get_item(k, j) for k in range(self.columns))
                result.set_item(i, j, value)

        return result
