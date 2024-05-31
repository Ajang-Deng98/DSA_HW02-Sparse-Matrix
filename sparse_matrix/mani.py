# This class represents a sparse matrix. 
# This class uses a dictionary to store the non-zero elements of the matrix.

from sparse_matrix import SparseMatrix

def main():
    print("Select the operation to perform:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    choice = input("Enter choice from these (1/2/3): ")

    file1 = input("easy_sample_03_3.txt: ")
    file2 = input("easy_sample_03_1.txt: ")

    matrixA = SparseMatrix(file1)
    matrixB = SparseMatrix(file2)

    if choice == '1':
        result = matrixA + matrixB
    elif choice == '2':
        result = matrixA - matrixB
    elif choice == '3':
        result = matrixA * matrixB
    else:
        print("Invalid choice")
        return

    print("Resultant Matrix:")
    print(result)

if __name__ == "__main__":
    main()
