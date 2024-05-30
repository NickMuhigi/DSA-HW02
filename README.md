#**Sparse-Matrix**


**__init__:** Initializes a sparse matrix. It can take either a file path to load the matrix from a file or the dimensions of the matrix (rows and columns). If a file path is provided, it loads the matrix from the file using the load_from_txt method. If dimensions are provided, it initializes an empty matrix.

**load_from_txt:** Loads the matrix from a text file. It reads the file, parses the dimensions from the first two lines, and then reads the remaining lines to populate the matrix.

**get_item:** Retrieves the value at a given row and column in the matrix. If the element is not present (i.e., it's zero), it returns 0.

**set_item:** Sets the value at a given row and column in the matrix. If the value is zero, it removes the element from the matrix.

**matrix_add:** Adds another sparse matrix to the current matrix. It creates a new matrix with the same dimensions and iterates through the union of keys (row, column pairs) of both matrices, adding corresponding values.

**matrix_subtract:** Subtracts another sparse matrix from the current matrix. Similar to matrix_add, it creates a new matrix with the same dimensions and iterates through the union of keys, subtracting corresponding values.

**matrix_multiply:** Multiplies the current matrix by another sparse matrix. It first checks if the number of columns in the first matrix is equal to the number of rows in the second matrix. Then, it performs matrix multiplication and stores the result in a new matrix.
