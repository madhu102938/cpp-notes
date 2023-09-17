Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy **all of the following rules**:

1. Each of the digits `1-9` must occur exactly once in each row.
2. Each of the digits `1-9` must occur exactly once in each column.
3. Each of the digits `1-9` must occur exactly once in each of the 9 `3x3` sub-boxes of the grid.

The `'.'` character indicates empty cells.

```cpp
class Solution {
public:
    // Function to check if placing 'num' at (row, col) is valid
    bool isValid(vector<vector<char>>& board, int row, int col, char num) {
        for (int i = 0; i < 9; i++) {
            // Check the row and column for conflicts with 'num'
            if (board[row][i] == num || board[i][col] == num)
                return false;

            // Check the 3x3 subgrid for conflicts with 'num'
            if (board[3 * (row / 3) + i / 3][3 * (col / 3) + i % 3] == num)
                return false;
        }
        return true; // 'num' can be safely placed at (row, col)
    }

    // Recursive function to solve the Sudoku puzzle
    bool solveSudoku(vector<vector<char>>& board) {
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] == '.') {
                    for (char c = '1'; c <= '9'; c++) {
                        if (isValid(board, i, j, c)) {
                            board[i][j] = c; // Place 'c' at (i, j)
                            if (solveSudoku(board))
                                return true; // Continue solving recursively
                            else {
                                board[i][j] = '.'; // Backtrack: remove 'c'
                            }
                        }
                    }
                    return false; // No valid number can be placed at (i, j)
                }
            }
        }
        return true; // The entire Sudoku has been filled successfully
    }
};

int main()
{
    Solution s;
    vector<vector<char>> board = 
    {
        {'5', '3', '.', '.', '7', '.', '.', '.', '.'}, 
        {'6', '.', '.', '1', '9', '5', '.', '.', '.'}, 
        {'.', '9', '8', '.', '.', '.', '.', '6', '.'}, 
        {'8', '.', '.', '.', '6', '.', '.', '.', '3'}, 
        {'4', '.', '.', '8', '.', '3', '.', '.', '1'}, 
        {'7', '.', '.', '.', '2', '.', '.', '.', '6'}, 
        {'.', '6', '.', '.', '.', '.', '2', '8', '.'}, 
        {'.', '.', '.', '4', '1', '9', '.', '.', '5'}, 
        {'.', '.', '.', '.', '8', '.', '.', '7', '9'}
    };    
    s.solveSudoku(board);
    for (int i = 0; i < 9; i++)
    {
        for (int j = 0; j < 9; j++)
        {
            cout << board[i][j];
            if (j % 3 == 2)
            {
                cout << " |";
            }
            else
                cout << " ";
        }
        cout << '\n';
        if (i % 3 == 2 && i != 8)
            cout << "_ _ _ _ _ _ _ _ _ _ _" << '\n';
    }
    return 0;
}
```