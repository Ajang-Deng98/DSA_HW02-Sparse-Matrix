class SparseMatrix:
    def __init__(self):
        self.rows = 0
        self.cols = 0
        self.data = {}
# This code defines a method called read_from_file within the SparseMatrix class. 
# This method is used to read the contents of a file and populate the sparse matrix object with the data from the file.
    def read_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith('rows='):
                    self.rows = int(line.split('=')[1])
                elif line.startswith('cols='):
                    self.cols = int(line.split('=')[1])
                else:
                    row, col, value = map(int, line.split())
                    if row not in self.data:
                        self.data[row] = {}
                    self.data[row][col] = value
# This code defines a special method called __str__ within the SparseMatrix class. 
# This method is used to provide a string representation of the sparse matrix object

    def __str__(self):
        output = [f"rows={self.rows}", f"cols={self.cols}"]
        for row in sorted(self.data.keys()):
            for col in sorted(self.data[row].keys()):
                output.append(f"({row}, {col}, {self.data[row][col]})")
        return "\n".join(output)

# The main block to execute the code and provide the output
if __name__ == "__main__":
    filename = 'easy_sample_01_3.txt'  
    sparse_matrix = SparseMatrix()
    sparse_matrix.read_from_file(filename)
    print(sparse_matrix)
