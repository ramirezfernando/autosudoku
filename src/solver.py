import pyautogui as pg

type IntMatrix = list[list[int]]
type StrMatrix = list[list[str]]

class Solver:
    def __init__(self, board: IntMatrix) -> None:
        """Solves online Sudoku puzzles.

        Args:
            board (list[list[int]]): The Sudoku puzzle board.
        Returns:
            None
        """
        self.board = board

    def isValid(self, row: int, col: int, number: int) -> bool:
        """Checks if a given number can be placed on the board while following Sudoku rules.

        Args:
            row (int): The row index on the board.
            col (int): The column index on the board.
            number (int): The number to be placed on the board.
        Returns:
            bool
        """
        for i in range(9):
            if self.board[row][i] == number:
                return False
            if self.board[i][col] == number:
                return False
            
        cornerRow = row - row % 3
        cornerCol = col - col % 3
        for x in range(3):
            for y in range(3):
                if self.board[cornerRow + x][cornerCol + y] == number:
                    return False
        return True
    
    def solve(self) -> None:
        """Solves the Sudoku puzzle.

        Args:
            None
        Returns:
            None
        """
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    for num in range(1, 10):
                        if self.isValid(row, col, num):
                            self.board[row][col] = num
                            self.solve()
                            self.board[row][col] = 0
                    return
        self.automate()

    def flatten(self, board: IntMatrix) -> StrMatrix:
        """Converts a matrix with integer values to a matrix with string values.

        Args:
            board (list[list[int]]): The Sudoku puzzle board.
        Returns:
            list[list[str]]
        """
        flatBoard = []
        for row in board:
            flatBoard.extend(row)

        return [str(num) for num in flatBoard]
    
    def automate(self) -> None:
        """Automates the process of solving the Sudoku puzzle.

        NOTE: Place your cursor on the top left corner of the online Sudoku puzzle board.

        Args:
            None
        Returns:
            None
        """
        flattenBoard = self.flatten(self.board)
        counter = 0
        
        for num in flattenBoard:
            pg.press(num)
            pg.hotkey('right')
            counter += 1
            if counter % 9 == 0:
                pg.hotkey('down')
                for _ in range(9):
                    pg.hotkey('left')

