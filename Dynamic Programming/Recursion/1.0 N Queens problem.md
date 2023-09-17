The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return _all distinct solutions to the **n-queens puzzle**_. You may return the answer in **any order**.

Each solution contains a distinct board configuration of the n-queens' placement, where `'Q'` and `'.'` both indicate a queen and an empty space, respectively.

### Solution (not as efficient)
```cpp
class Solution {
public:
    // Function to check if placing a queen at (row, col) is safe
    bool isSafe1(int row, int col, vector<string>& board, int n) {
        int duprow = row;
        int dupcol = col;

        // Check upper left diagonal
        while (row >= 0 && col >= 0) {
            if (board[row][col] == 'Q')
                return false;
            row--;
            col--;
        }

        // Reset row and col to original values
        col = dupcol;
        row = duprow;

        // Check left column
        while (col >= 0) {
            if (board[row][col] == 'Q')
                return false;
            col--;
        }

        // Reset row and col to original values
        row = duprow;
        col = dupcol;

        // Check lower left diagonal
        while (row < n && col >= 0) {
            if (board[row][col] == 'Q')
                return false;
            row++;
            col--;
        }
        return true; // It's safe to place a queen at (row, col)
    }

public:
    // Recursive function to solve N-Queens problem
    void solve(int col, vector<string>& board, vector<vector<string>>& ans, int n) {
        if (col == n) {
            ans.push_back(board); // If all queens are placed, add the current configuration to the answer
            return;
        }
        for (int row = 0; row < n; row++) {
            if (isSafe1(row, col, board, n)) { // Check if it's safe to place a queen at (row, col)
                board[row][col] = 'Q'; // Place the queen
                solve(col + 1, board, ans, n); // Recur for the next column
                board[row][col] = '.'; // Backtrack: remove the queen and try another position
            }
        }
    }

public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> ans; // To store all possible solutions
        vector<string> board(n); // Initialize the board with empty strings
        string s(n, '.'); // Create a string of '.' of length n
        for (int i = 0; i < n; i++) {
            board[i] = s; // Initialize each row of the board with the string of '.'s
        }
        solve(0, board, ans, n); // Start solving the N-Queens problem from the first column
        return ans; // Return the list of all valid solutions
    }
};
```




### Efficient Solution
```cpp
class Solution {
public:
    // Recursive function to solve N-Queens problem
    void solve(int col, vector<string>& board, vector<vector<string>>& ans,
               vector<int>& leftrow, vector<int>& upperDiagonal, vector<int>& lowerDiagonal, int n) {
        if (col == n) {
            ans.push_back(board); // If all queens are placed, add the current configuration to the answer
            return;
        }
        for (int row = 0; row < n; row++) {
            // Check if it's safe to place a queen at (row, col) using the precomputed arrays
            if (leftrow[row] == 0 && lowerDiagonal[row + col] == 0 && upperDiagonal[n - 1 + col - row] == 0) {
                board[row][col] = 'Q'; // Place the queen
                leftrow[row] = 1;
                lowerDiagonal[row + col] = 1;
                upperDiagonal[n - 1 + col - row] = 1;
                solve(col + 1, board, ans, leftrow, upperDiagonal, lowerDiagonal, n); // Recur for the next column
                board[row][col] = '.'; // Backtrack: remove the queen and try another position
                leftrow[row] = 0;
                lowerDiagonal[row + col] = 0;
                upperDiagonal[n - 1 + col - row] = 0;
            }
        }
    }

public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> ans; // To store all possible solutions
        vector<string> board(n); // Initialize the board with empty strings
        string s(n, '.'); // Create a string of '.' of length n
        for (int i = 0; i < n; i++) {
            board[i] = s; // Initialize each row of the board with the string of '.'s
        }
        vector<int> leftrow(n, 0), upperDiagonal(2 * n - 1, 0), lowerDiagonal(2 * n - 1, 0);
        solve(0, board, ans, leftrow, upperDiagonal, lowerDiagonal, n); // Start solving the N-Queens problem from the first column
        return ans; // Return the list of all valid solutions
    }
};
```

In the N-Queens problem, `leftrow`, `upperDiagonal`, and `lowerDiagonal` vectors are used to keep track of safe positions for placing queens on the chessboard. Let's go through each of these vectors and their purposes:

1. `leftrow` Vector:
    
    - The `leftrow` vector is used to keep track of whether a row is safe for placing a queen or not.
    - Each element in the vector corresponds to a row on the chessboard.
    - If `leftrow[row]` is `0`, it means that the row `row` is currently safe for placing a queen.
    - If `leftrow[row]` is `1`, it means that a queen is already placed in the row `row`, and hence, it's not safe to place another queen in that row.
2. `upperDiagonal` and `lowerDiagonal` Vectors:
    
    - The `upperDiagonal` and `lowerDiagonal` vectors are used to keep track of whether a diagonal is safe for placing a queen or not.
    - Diagonals in a chessboard are determined by the sum of row and column indices, and the difference of row and column indices.
    - For an `n x n` chessboard, there are `2*n - 1` diagonals: `n` diagonals going from the top-left to the bottom-right, and `n - 1` diagonals going from the top-right to the bottom-left.
    - Each element in the vectors corresponds to a diagonal index.
    - If `upperDiagonal[i]` is `0`, it means that the diagonal with index `i` is currently safe for placing a queen.
    - If `upperDiagonal[i]` is `1`, it means that a queen is already placed on the diagonal with index `i`, and hence, it's not safe to place another queen on that diagonal.
    - Similarly, the same logic applies to the `lowerDiagonal` vector.

The purpose of using these vectors is to efficiently determine whether a specific position (row, column) on the chessboard is safe for placing a queen by checking the conditions for the row and both diagonals passing through that position. These vectors help in reducing the time complexity of the solution by avoiding redundant checks and improving the overall efficiency of the algorithm.