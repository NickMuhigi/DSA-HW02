**SparseMatrix class:**

This class represents a sparse matrix and contains methods to perform various operations on sparse matrices.
The constructor (__init__) initializes the SparseMatrix object. It can be initialized either by providing a file path to load the matrix from, or by specifying the number of rows and columns directly.
The load_from_file method reads the matrix from a file. It parses the file line by line, extracting the number of rows and columns from the first two lines, and the matrix entries from subsequent lines. Each entry is in the format (row, column, value).
The get_element method returns the value at a specified position in the matrix. If the position is not explicitly set in the matrix, it returns 0 (as per sparse matrix definition).
The set_element method sets the value at a specified position in the matrix. If the value is 0, it removes the entry from the matrix to maintain sparsity.
The add, subtract, and multiply methods perform addition, subtraction, and multiplication operations on two sparse matrices, respectively. These methods iterate over the non-zero elements of both matrices and compute the result matrix accordingly.



**File Organization:**


The code is organized into a directory structure where the main Python script sparse_matrix.py is located in /dsa/sparse_matrix/code/src/.
Sample input files and result files are stored in the /dsa/sparse_matrix/sample_inputs/ directory.



**Handling Variations in Input File:**

The code handles variations in the input file format by parsing the file contents and extracting relevant information (number of rows, columns, and matrix entries).
If the file has any whitespaces on some lines, they are ignored during parsing.
If the file has a wrong format (e.g., different parentheses or floating-point values), the code raises a ValueError with an appropriate error message.
