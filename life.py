from abc import abstractmethod, ABC
from time import sleep



class AbstractLifeGameBoard(ABC):
    def __init__(self, width: int = 6, height: int = 6):
        pass

    def __str__(self):
        """Return a string representation of a board.

        Use small o for alive cells and period for empty cells.
        E.g. for board 3x3 with simplest oscillator:
        .o.
        .o.
        .o.
        """
        pass

    @abstractmethod
    def place_cell(self, row: int, col: int):
        """Make a cell alive."""
        pass

    @abstractmethod
    def toggle_cell(self, row: int, col: int) -> None:
        """Invert state of the cell."""
        pass

    @abstractmethod
    def next(self) -> None:
        pass

    @abstractmethod
    def is_alive(self, row: int, col: int) -> bool:
        pass


class Board(AbstractLifeGameBoard):
    """Put your solution here"""
    def __init__(self,height,width):
        self.board = []
        self.height = height
        self.width = width
        for i in range(3):
            row = []
            for j in range(3):
                row.append(False)
            self.board.append(row)

    def __str__(self):
        result = ""
        for row in self.board:
            for cell in row:
                if cell:
                    result += "0"
                else:
                    result += "."
            result += "\n"
        return result
    def is_alive(self, row: int, col: int):
        try:
            if row<0 or row>=self.height:
                raise IndexError
            if col<0 or col>=self.width:
                raise IndexError
        except IndexError:
            result = False
            return result

        return self.board[col][row]

    def place_cell(self, row: int, col: int):
        self.board[col][row] = True

    def toggle_cell(self, row: int, col: int) -> None:
        self.board[col][row] = not self.board[col][row]
    def liveness_tester(self,row: int,col: int):
        neibours = 0
        for i in range(-1,2):
            for j in range(-1,2):
                if i==0 and j==0:
                    continue
                neibours += self.is_alive(row+i, col+j)
        return neibours
    def next(self) -> None:
        new_board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            new_board.append(row)

        for index_X in range(len(self.board)) :
            for index_Y in range(self.width):
                state = False
                neibour_count = self.liveness_tester(index_X, index_Y)
                if neibour_count == 2 and self.is_alive(index_X,index_Y):
                    state = True
                elif neibour_count == 3 and self.is_alive(index_X,index_Y):
                    state = True
                elif neibour_count == 3 and not self.is_alive(index_X,index_Y):
                    state = True
                new_board[index_Y][index_X] = state
        self.board = new_board









c = CELL_SYMBOL = "o"


if __name__ == "__main__":
    board = Board(3, 3)
    for i in range(3):
        board.place_cell(1, i)

    for i in range(100):
        print(board)
        board.next()
        sleep(0.5)

#order of operations: is_alive, next, place_cell, toggle_cell