# This class represents a sparse matrix, which is a matrix where most of the elements are zero
class SparseMatrix:

# This is the constructor method for a class SparseMatrix. It takes three optional arguments: file_path, num_rows, and num_cols.
    def __init__(self, file_path=None, num_rows=None, num_cols=None):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.values = {}  # {(row, col): value}

        if file_path:
            self._load_from_file(file_path)

# This method of a class takes a file path as an argument and loads the matrix from the file.

    def _load_from_file(self, file_path):
        try:
            with open(file_path, 'r') as f:
                lines = f.readlines()
                self.num_rows = int(lines[0].split('=')[1])
                self.num_cols = int(lines[1].split('=')[1])
                for line in lines[2:]:
                    if line.strip():  # Ignore empty lines
                        row, col, val = map(int, line.strip('()\n').split(','))
                        self.set_element(row, col, val)
        except Exception as e:
            raise ValueError(f"Error reading file: {e}")
        
# This method of a class takes two arguments, row and col, which are indices of a matrix element.

    def get_element(self, row, col):
        return self.values.get((row, col), 0)

    def set_element(self, row, col, value):
        if value != 0:
            self.values[(row, col)] = value
        elif (row, col) in self.values:
            del self.values[(row, col)]

# This method, __add__,  It defines the addition operation between two instances of this class.
    def __add__(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrix dimensions must match for addition")
        result = SparseMatrix(num_rows=self.num_rows, num_cols=self.num_cols)
        for (row, col), val in self.values.items():
            result.set_element(row, col, val + other.get_element(row, col))
        for (row, col), val in other.values.items():
            if (row, col) not in self.values:
                result.set_element(row, col, val)
        return result

# This method __sub__ defines the subtraction operation between two instances of a class called SparseMatrix.
    def __sub__(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrix dimensions must match for subtraction")
        result = SparseMatrix(num_rows=self.num_rows, num_cols=self.num_cols)
        for (row, col), val in self.values.items():
            result.set_element(row, col, val - other.get_element(row, col))
        for (row, col), val in other.values.items():
            if (row, col) not in self.values:
                result.set_element(row, col, -val)
        return result

# This method, __mul__,  It defines the multiplication operation between two instances of this class.
    def __mul__(self, other):
        if self.num_cols != other.num_rows:
            raise ValueError("Number of columns of A must equal number of rows of B for multiplication")
        result = SparseMatrix(num_rows=self.num_rows, num_cols=other.num_cols)
        for (row, col), val in self.values.items():
            for k in range(other.num_cols):
                result.set_element(row, k, result.get_element(row, k) + val * other.get_element(col, k))
        return result

    def __str__(self):
        result = f"rows={self.num_rows}\ncols={self.num_cols}\n"
        for (row, col), val in sorted(self.values.items()):
            result += f"({row}, {col}, {val})\n"
        return result
